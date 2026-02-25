import { NextResponse } from "next/server";

export async function POST(request: Request) {
  const { item, verdict, score } = await request.json();

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
    return NextResponse.json({
      name: "Simple " + trimmed + " bowl",
      ingredients: ["Could not connect to AI — try again later"],
      description: "Recipe suggestions require an AI connection.",
    });
  }

  const context =
    verdict === "trash"
      ? `The user just looked up "${trimmed}" which scored ${score}/100 and was rated TRASH. Suggest a healthier whole-food alternative recipe inspired by the same flavour profile or craving.`
      : `The user just looked up "${trimmed}" which scored ${score}/100 and was rated FOOD. Suggest a delicious whole-food recipe that features this ingredient as the star.`;

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
              content: `You suggest simple whole-food recipes. Rules:
- Only use real, unprocessed ingredients humans evolved to eat
- NO seed oils (canola, soybean, sunflower, corn, safflower, cottonseed, grapeseed)
- NO refined sugar, NO refined flour, NO artificial ingredients
- Allowed fats: butter, ghee, tallow, lard, olive oil, coconut oil, avocado oil
- Keep it to 4-6 ingredients maximum
- Recipes should be practical and easy to make

Reply with EXACTLY three lines:
Line 1: A short, catchy recipe name (no quotes)
Line 2: Comma-separated list of ingredients (just names, no quantities)
Line 3: A 2-3 sentence description of how to make it. Keep it casual and appetising.`,
            },
            {
              role: "user",
              content: context,
            },
          ],
          max_tokens: 200,
        }),
      }
    );

    if (!response.ok) {
      return NextResponse.json({
        name: "Grilled " + trimmed,
        ingredients: ["Could not generate a recipe — try again"],
        description: "The AI is taking a break. Try again in a moment.",
      });
    }

    const data = await response.json();
    const text: string = data.result?.response || "";
    const lines = text
      .trim()
      .split("\n")
      .map((l: string) => l.trim())
      .filter((l: string) => l.length > 0);

    const name = (lines[0] || "Whole food recipe")
      .replace(/^["']|["']$/g, "")
      .replace(/^\d+[\.\)]\s*/, "");

    const ingredients =
      lines.length > 1
        ? lines[1]
            .split(",")
            .map((s: string) => s.trim().replace(/^["']|["']$/g, ""))
            .filter((s: string) => s.length > 0)
        : [trimmed];

    const description =
      lines.length > 2
        ? lines
            .slice(2)
            .join(" ")
            .trim()
        : `A simple, delicious recipe featuring ${trimmed}.`;

    return NextResponse.json({ name, ingredients, description });
  } catch {
    return NextResponse.json({
      name: "Simple " + trimmed + " dish",
      ingredients: ["Could not generate a recipe — try again"],
      description: "Something went wrong. Give it another try.",
    });
  }
}
