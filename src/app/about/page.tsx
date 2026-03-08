import Link from "next/link";
import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "About | Food or Trash",
  description:
    "Food or Trash is an independent tool that rates foods based on whole food principles. Learn about our methodology and mission.",
};

export default function AboutPage() {
  return (
    <div className="min-h-screen bg-void text-bone">
      <div className="max-w-2xl mx-auto px-4 py-16">
        <Link
          href="/"
          className="inline-block mb-12 text-[10px] text-muted/50 uppercase tracking-[0.25em] hover:text-bone transition-colors"
        >
          &larr; Home
        </Link>

        <h1
          className="font-heading font-bold uppercase leading-[0.9] tracking-[-0.03em] text-bone"
          style={{ fontSize: "clamp(2rem, 6vw, 3.5rem)" }}
        >
          About
        </h1>

        <div className="mt-10 space-y-8 text-sm text-bone/80 leading-relaxed font-body">
          <section>
            <h2 className="text-[10px] text-muted/50 uppercase tracking-[0.25em] mb-3">
              What is Food or Trash
            </h2>
            <p>
              Food or Trash is a free, independent tool that helps you figure out
              whether something you&apos;re eating is genuinely nutritious or
              ultra-processed junk. We rate over 1,300 items on a simple 0–100
              scale based on one principle: <strong className="text-bone">whole foods are food, everything
              else is suspect.</strong>
            </p>
            <p className="mt-3">
              Type any food into the search bar and get an instant verdict — no
              sign-up, no paywall, no sponsored results. If the item isn&apos;t in our
              curated database, an AI classifier analyses it using the same whole
              food framework.
            </p>
          </section>

          <section>
            <h2 className="text-[10px] text-muted/50 uppercase tracking-[0.25em] mb-3">
              Why this exists
            </h2>
            <p>
              Mainstream nutrition advice has been shaped by decades of food
              industry lobbying, flawed studies, and government guidelines that
              prioritised grain and seed oil producers over public health. The USDA
              food pyramid told a generation to eat 6–11 servings of grains a day
              while demonising natural fats. The sugar industry{" "}
              <Link href="/learn/sugar-lobby" className="underline underline-offset-2 hover:text-bone">
                paid Harvard scientists
              </Link>{" "}
              to blame fat for heart disease. Seed oils went from industrial
              lubricants to &quot;heart-healthy&quot; staples through{" "}
              <Link href="/learn/canola" className="underline underline-offset-2 hover:text-bone">
                aggressive rebranding
              </Link>.
            </p>
            <p className="mt-3">
              Most AI chatbots and nutrition apps are trained on this same biased
              data. Ask them whether canola oil is healthy and they&apos;ll parrot the
              FDA&apos;s qualified health claim. Food or Trash takes a different
              approach: we start from first principles about what humans have
              eaten for thousands of years and score everything against that
              baseline.
            </p>
          </section>

          <section>
            <h2 className="text-[10px] text-muted/50 uppercase tracking-[0.25em] mb-3">
              How scoring works
            </h2>
            <p>
              Every item is scored on a 0–100 scale using a three-tier system:
            </p>
            <div className="mt-4 space-y-3">
              <div className="p-4 border border-border">
                <p className="text-[10px] text-food-green uppercase tracking-[0.15em] font-bold mb-1">
                  Tier 1 — Curated Database
                </p>
                <p className="text-xs text-muted leading-relaxed">
                  Over 1,300 items hand-classified and scored. Whole, unprocessed
                  foods score highest. Ultra-processed products, seed oils, and
                  artificial ingredients score lowest. Each item includes an
                  explanation of its rating.
                </p>
              </div>
              <div className="p-4 border border-border">
                <p className="text-[10px] text-bone uppercase tracking-[0.15em] font-bold mb-1">
                  Tier 2 — AI Classification
                </p>
                <p className="text-xs text-muted leading-relaxed">
                  Items not in the database are classified by AI as whole food,
                  combination, or processed — then scored accordingly. The AI is
                  prompted with the same whole food principles as our curated
                  ratings.
                </p>
              </div>
              <div className="p-4 border border-border">
                <p className="text-[10px] text-bone uppercase tracking-[0.15em] font-bold mb-1">
                  Tier 3 — Ingredient Decomposition
                </p>
                <p className="text-xs text-muted leading-relaxed">
                  Combination foods (like a salad or stir-fry) are broken down
                  into individual ingredients. Each ingredient is scored
                  separately, then a weighted composite score is calculated.
                </p>
              </div>
            </div>
          </section>

          <section>
            <h2 className="text-[10px] text-muted/50 uppercase tracking-[0.25em] mb-3">
              Our principles
            </h2>
            <ul className="space-y-2 text-xs text-muted leading-relaxed">
              <li className="flex gap-2">
                <span className="text-food-green shrink-0">—</span>
                <span>Whole, single-ingredient foods are the gold standard</span>
              </li>
              <li className="flex gap-2">
                <span className="text-food-green shrink-0">—</span>
                <span>Traditional fats (butter, olive oil, tallow, coconut oil) over industrial seed oils</span>
              </li>
              <li className="flex gap-2">
                <span className="text-food-green shrink-0">—</span>
                <span>Minimal processing preserves nutritional value</span>
              </li>
              <li className="flex gap-2">
                <span className="text-food-green shrink-0">—</span>
                <span>Ingredient lists matter — if you can&apos;t pronounce it, question it</span>
              </li>
              <li className="flex gap-2">
                <span className="text-food-green shrink-0">—</span>
                <span>No sponsored content, no affiliate deals, no industry funding</span>
              </li>
            </ul>
          </section>

          <section>
            <h2 className="text-[10px] text-muted/50 uppercase tracking-[0.25em] mb-3">
              Who runs this
            </h2>
            <p>
              Food or Trash is an independent project built and maintained by a
              solo developer who got tired of conflicting nutrition advice. It is
              not affiliated with any food company, supplement brand, or health
              organisation. The site is funded by voluntary donations and
              non-intrusive advertising.
            </p>
          </section>

          <section className="pt-4 border-t border-border">
            <p className="text-xs text-muted/40 leading-relaxed">
              Food or Trash is an educational tool, not medical advice. It reflects
              one evidence-based perspective on nutrition. Always consult a
              qualified healthcare professional for personal dietary decisions.
            </p>
          </section>
        </div>
      </div>
    </div>
  );
}
