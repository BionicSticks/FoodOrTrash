import Link from "next/link";
import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "Terms of Use | Food or Trash",
  description:
    "Terms of use for foodortrash.com. Understand the conditions of using this site.",
};

export default function TermsPage() {
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
          Terms of Use
        </h1>

        <p className="mt-4 text-xs text-muted/50">
          Last updated: March 2026
        </p>

        <div className="mt-10 space-y-8 text-sm text-bone/80 leading-relaxed font-body">
          <section>
            <h2 className="text-[10px] text-muted/50 uppercase tracking-[0.25em] mb-3">
              Acceptance of terms
            </h2>
            <p>
              By accessing and using Food or Trash (&quot;the site&quot;,
              &quot;foodortrash.com&quot;), you agree to be bound by these terms
              of use. If you do not agree with any part of these terms, please do
              not use the site.
            </p>
          </section>

          <section>
            <h2 className="text-[10px] text-muted/50 uppercase tracking-[0.25em] mb-3">
              Not medical advice
            </h2>
            <p>
              Food or Trash is an educational and informational tool. The food
              ratings, scores, explanations, and all other content on this site are
              provided for general information purposes only and{" "}
              <strong className="text-bone">
                do not constitute medical, nutritional, or dietary advice
              </strong>
              .
            </p>
            <p className="mt-3">
              The information presented reflects one evidence-based perspective on
              nutrition and may not be suitable for your individual health needs,
              medical conditions, or dietary requirements. Always consult a
              qualified healthcare professional, registered dietitian, or doctor
              before making changes to your diet, especially if you have
              allergies, intolerances, chronic conditions, or are taking
              medication.
            </p>
          </section>

          <section>
            <h2 className="text-[10px] text-muted/50 uppercase tracking-[0.25em] mb-3">
              Accuracy of information
            </h2>
            <p>
              We make reasonable efforts to ensure the accuracy of our food
              database and AI classification system. However, we do not guarantee
              that all ratings, scores, or classifications are complete, current,
              or error-free. Food composition and processing methods vary by brand,
              region, and preparation.
            </p>
            <p className="mt-3">
              AI-generated classifications (for items not in our curated database)
              are best-effort assessments and may occasionally produce inaccurate
              results. Use your own judgement and verify with product labels.
            </p>
          </section>

          <section>
            <h2 className="text-[10px] text-muted/50 uppercase tracking-[0.25em] mb-3">
              Use of the site
            </h2>
            <p>You agree to use the site only for lawful purposes. You may not:</p>
            <ul className="mt-3 space-y-2 text-xs text-muted leading-relaxed">
              <li className="flex gap-2">
                <span className="text-trash-red shrink-0">—</span>
                <span>Scrape, reproduce, or redistribute our database for commercial purposes</span>
              </li>
              <li className="flex gap-2">
                <span className="text-trash-red shrink-0">—</span>
                <span>Abuse the AI classification API with excessive automated requests</span>
              </li>
              <li className="flex gap-2">
                <span className="text-trash-red shrink-0">—</span>
                <span>Misrepresent the site&apos;s ratings as professional medical or dietary advice</span>
              </li>
              <li className="flex gap-2">
                <span className="text-trash-red shrink-0">—</span>
                <span>Attempt to disrupt or interfere with the site&apos;s operation</span>
              </li>
            </ul>
          </section>

          <section>
            <h2 className="text-[10px] text-muted/50 uppercase tracking-[0.25em] mb-3">
              Intellectual property
            </h2>
            <p>
              All content on this site — including text, ratings, design, code, and
              branding — is the property of Food or Trash unless otherwise stated.
              The educational articles in our &quot;How We Got Here&quot; section
              reference publicly available research, which is cited with sources.
            </p>
          </section>

          <section>
            <h2 className="text-[10px] text-muted/50 uppercase tracking-[0.25em] mb-3">
              Third-party content
            </h2>
            <p>
              The site links to external resources including research papers,
              books, and videos. We are not responsible for the content, accuracy,
              or availability of these external sites. Links do not imply
              endorsement.
            </p>
          </section>

          <section>
            <h2 className="text-[10px] text-muted/50 uppercase tracking-[0.25em] mb-3">
              Limitation of liability
            </h2>
            <p>
              Food or Trash is provided &quot;as is&quot; without warranties of any
              kind, express or implied. To the fullest extent permitted by law, we
              shall not be liable for any damages arising from your use of the
              site, reliance on its content, or inability to access the site.
            </p>
          </section>

          <section>
            <h2 className="text-[10px] text-muted/50 uppercase tracking-[0.25em] mb-3">
              Changes to these terms
            </h2>
            <p>
              We reserve the right to update these terms at any time. Changes take
              effect when posted on this page. Continued use of the site after
              changes constitutes acceptance of the new terms.
            </p>
          </section>

          <section>
            <h2 className="text-[10px] text-muted/50 uppercase tracking-[0.25em] mb-3">
              Contact
            </h2>
            <p>
              Questions about these terms? Email{" "}
              <a
                href="mailto:hello@foodortrash.com"
                className="underline underline-offset-2 hover:text-bone"
              >
                hello@foodortrash.com
              </a>
              .
            </p>
          </section>
        </div>
      </div>
    </div>
  );
}
