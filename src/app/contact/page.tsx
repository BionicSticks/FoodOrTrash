import Link from "next/link";
import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "Contact | Food or Trash",
  description:
    "Get in touch with the Food or Trash team. Report issues, suggest foods, or ask questions.",
};

export default function ContactPage() {
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
          Contact
        </h1>

        <div className="mt-10 space-y-8 text-sm text-bone/80 leading-relaxed font-body">
          <section>
            <p>
              Food or Trash is an independent project maintained by a solo
              developer. Whether you&apos;ve found a bug, want to suggest a food
              to add, or have a question about how scoring works — I&apos;d like
              to hear from you.
            </p>
          </section>

          <section>
            <h2 className="text-[10px] text-muted/50 uppercase tracking-[0.25em] mb-4">
              Get in touch
            </h2>
            <div className="space-y-3">
              <div className="p-5 border border-border">
                <p className="text-[10px] text-bone uppercase tracking-[0.15em] font-bold mb-2">
                  General enquiries
                </p>
                <a
                  href="mailto:hello@foodortrash.com"
                  className="text-sm text-muted underline underline-offset-2 hover:text-bone transition-colors"
                >
                  hello@foodortrash.com
                </a>
              </div>
            </div>
          </section>

          <section>
            <h2 className="text-[10px] text-muted/50 uppercase tracking-[0.25em] mb-4">
              Common reasons to get in touch
            </h2>
            <div className="space-y-3">
              <div className="p-4 border border-border">
                <p className="text-[10px] text-bone uppercase tracking-[0.15em] font-bold mb-1">
                  Suggest a food
                </p>
                <p className="text-xs text-muted leading-relaxed">
                  Think something is missing from our database? Let us know what
                  food or product you&apos;d like to see rated.
                </p>
              </div>
              <div className="p-4 border border-border">
                <p className="text-[10px] text-bone uppercase tracking-[0.15em] font-bold mb-1">
                  Report an error
                </p>
                <p className="text-xs text-muted leading-relaxed">
                  Found a rating you disagree with or a factual error? We take
                  accuracy seriously and will review your feedback.
                </p>
              </div>
              <div className="p-4 border border-border">
                <p className="text-[10px] text-bone uppercase tracking-[0.15em] font-bold mb-1">
                  Technical issues
                </p>
                <p className="text-xs text-muted leading-relaxed">
                  Something broken or not working as expected? Include your
                  browser, device, and a description of the issue.
                </p>
              </div>
            </div>
          </section>

          <section>
            <h2 className="text-[10px] text-muted/50 uppercase tracking-[0.25em] mb-4">
              Support the project
            </h2>
            <p>
              Food or Trash is free to use and has no paywalls. If you find it
              useful, you can support ongoing development and hosting costs:
            </p>
            <div className="mt-4">
              <a
                href="https://ko-fi.com/foodortrash"
                target="_blank"
                rel="noopener noreferrer"
                className="inline-block px-6 py-3 text-xs font-body font-semibold uppercase tracking-[0.2em] text-bone/70 border border-border hover:border-bone/30 hover:text-bone transition-all"
              >
                Support on Ko-fi
              </a>
            </div>
          </section>
        </div>
      </div>
    </div>
  );
}
