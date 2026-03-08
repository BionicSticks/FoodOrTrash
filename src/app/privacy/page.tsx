import Link from "next/link";
import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "Privacy Policy | Food or Trash",
  description:
    "Privacy policy for foodortrash.com. Learn how we handle your data.",
};

export default function PrivacyPage() {
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
          Privacy Policy
        </h1>

        <p className="mt-4 text-xs text-muted/50">
          Last updated: March 2026
        </p>

        <div className="mt-10 space-y-8 text-sm text-bone/80 leading-relaxed font-body">
          <section>
            <h2 className="text-[10px] text-muted/50 uppercase tracking-[0.25em] mb-3">
              Overview
            </h2>
            <p>
              Food or Trash (&quot;we&quot;, &quot;the site&quot;) is committed to
              protecting your privacy. This policy explains what data we collect,
              how we use it, and your rights regarding that data.
            </p>
            <p className="mt-3">
              The short version: we collect minimal data, we don&apos;t require
              accounts, and we don&apos;t sell your information to anyone.
            </p>
          </section>

          <section>
            <h2 className="text-[10px] text-muted/50 uppercase tracking-[0.25em] mb-3">
              Data we collect
            </h2>

            <div className="space-y-4">
              <div className="p-4 border border-border">
                <p className="text-[10px] text-bone uppercase tracking-[0.15em] font-bold mb-2">
                  Analytics (Vercel Analytics)
                </p>
                <p className="text-xs text-muted leading-relaxed">
                  We use Vercel Analytics to understand how visitors use the site.
                  This collects anonymous, aggregated data such as page views,
                  referral sources, and general geographic region. No personally
                  identifiable information is collected. Vercel Analytics is
                  privacy-focused and does not use cookies for tracking.
                </p>
              </div>

              <div className="p-4 border border-border">
                <p className="text-[10px] text-bone uppercase tracking-[0.15em] font-bold mb-2">
                  Advertising (Google AdSense)
                </p>
                <p className="text-xs text-muted leading-relaxed">
                  We display advertisements through Google AdSense, which may use
                  cookies and similar technologies to serve ads based on your
                  browsing history. Google&apos;s use of advertising cookies is
                  governed by{" "}
                  <a
                    href="https://policies.google.com/privacy"
                    target="_blank"
                    rel="noopener noreferrer"
                    className="underline underline-offset-2 hover:text-bone"
                  >
                    Google&apos;s Privacy Policy
                  </a>
                  . You can opt out of personalised advertising by visiting{" "}
                  <a
                    href="https://www.google.com/settings/ads"
                    target="_blank"
                    rel="noopener noreferrer"
                    className="underline underline-offset-2 hover:text-bone"
                  >
                    Google Ads Settings
                  </a>
                  .
                </p>
              </div>

              <div className="p-4 border border-border">
                <p className="text-[10px] text-bone uppercase tracking-[0.15em] font-bold mb-2">
                  Search Queries
                </p>
                <p className="text-xs text-muted leading-relaxed">
                  When you search for a food item that isn&apos;t in our local
                  database, the query is sent to our AI classification service
                  (Cloudflare Workers AI) for analysis. These queries are processed
                  in real time and are not stored or logged by us. Cloudflare&apos;s
                  data handling is governed by their own privacy policy.
                </p>
              </div>
            </div>
          </section>

          <section>
            <h2 className="text-[10px] text-muted/50 uppercase tracking-[0.25em] mb-3">
              Data we do not collect
            </h2>
            <ul className="space-y-2 text-xs text-muted leading-relaxed">
              <li className="flex gap-2">
                <span className="text-food-green shrink-0">—</span>
                <span>No user accounts or registration</span>
              </li>
              <li className="flex gap-2">
                <span className="text-food-green shrink-0">—</span>
                <span>No email addresses, names, or personal details</span>
              </li>
              <li className="flex gap-2">
                <span className="text-food-green shrink-0">—</span>
                <span>No search history stored on our servers</span>
              </li>
              <li className="flex gap-2">
                <span className="text-food-green shrink-0">—</span>
                <span>No data sold to third parties</span>
              </li>
            </ul>
          </section>

          <section>
            <h2 className="text-[10px] text-muted/50 uppercase tracking-[0.25em] mb-3">
              Cookies
            </h2>
            <p>
              Food or Trash itself does not set any cookies. However, third-party
              services embedded on the site (Google AdSense) may set their own
              cookies. You can manage cookie preferences through your browser
              settings.
            </p>
          </section>

          <section>
            <h2 className="text-[10px] text-muted/50 uppercase tracking-[0.25em] mb-3">
              Your rights
            </h2>
            <p>
              Since we don&apos;t collect personal data, there is typically nothing
              to request access to or delete. If you have questions about your
              data or this policy, you can contact us at the address below.
            </p>
          </section>

          <section>
            <h2 className="text-[10px] text-muted/50 uppercase tracking-[0.25em] mb-3">
              Third-party links
            </h2>
            <p>
              The site contains links to external resources (research papers, books,
              videos). We are not responsible for the privacy practices of those
              external sites.
            </p>
          </section>

          <section>
            <h2 className="text-[10px] text-muted/50 uppercase tracking-[0.25em] mb-3">
              Changes to this policy
            </h2>
            <p>
              We may update this privacy policy from time to time. Changes will be
              reflected on this page with an updated date.
            </p>
          </section>

          <section>
            <h2 className="text-[10px] text-muted/50 uppercase tracking-[0.25em] mb-3">
              Contact
            </h2>
            <p>
              For privacy-related questions, email{" "}
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
