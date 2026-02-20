import { NextResponse } from "next/server";

export async function POST(request: Request) {
  const { item } = await request.json();

  if (!item || typeof item !== "string" || item.trim().length === 0) {
    return NextResponse.json(
      { error: "Item is required" },
      { status: 400 }
    );
  }

  const trimmed = item.trim().slice(0, 200);

  const accountId = process.env.CLOUDFLARE_ACCOUNT_ID;
  const apiKey = process.env.CLOUDFLARE_API_KEY;

  if (!accountId || !apiKey) {
    // No AI configured — make a best guess based on the query
    return NextResponse.json({
      isFood: false,
      reason: "Couldn't verify this one. When in doubt... trash.",
    });
  }

  try {
    const response = await fetch(
      `https://api.cloudflare.com/client/v4/accounts/${accountId}/ai/run/@cf/meta/llama-3.1-8b-instruct`,
      {
        method: "POST",
        headers: {
          Authorization: `Bearer ${apiKey}`,
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          messages: [
            {
              role: "system",
              content:
                "You are a strict whole-food evaluator. FOOD means: whole, unprocessed foods that humans evolved to eat — meat, fish, eggs, vegetables, fruits, nuts, seeds, traditional fats (butter, ghee, tallow, lard, olive oil, coconut oil, avocado oil). TRASH means: anything containing seed oils (canola, soybean, corn, sunflower, safflower, cottonseed, grapeseed oil), ultra-processed foods, artificial ingredients, refined sugars, or industrially produced ingredients. Reply with exactly 'Yes' (it is real food) or 'No' (it is trash) on the first line, then one punchy sentence explaining why on the second line. Be opinionated and direct.",
            },
            {
              role: "user",
              content: `Is "${trimmed}" real food or trash?`,
            },
          ],
          max_tokens: 80,
        }),
      }
    );

    if (!response.ok) {
      return NextResponse.json({
        isFood: false,
        reason: "Couldn't verify this one. When in doubt... trash.",
      });
    }

    const data = await response.json();
    const text: string = data.result?.response || "";
    const lines = text.trim().split("\n");
    const firstLine = lines[0]?.toLowerCase().trim() || "";
    const isFood = firstLine.startsWith("yes");
    const reason =
      lines.length > 1
        ? lines.slice(1).join(" ").trim()
        : isFood
          ? "The AI says this counts as food."
          : "The AI says this is definitely not food.";

    return NextResponse.json({ isFood, reason });
  } catch {
    return NextResponse.json({
      isFood: false,
      reason: "Couldn't verify this one. When in doubt... trash.",
    });
  }
}
