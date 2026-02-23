"use client";

import { motion } from "framer-motion";
import { FoodChecker } from "@/components/food-checker";
import { Background } from "@/components/background";

export default function Home() {
  return (
    <>
      <Background />
      <main className="relative min-h-screen flex flex-col items-center justify-center px-4 py-20 overflow-hidden">
      {/* Hero */}
      <motion.div
        initial={{ opacity: 0, y: 40 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.8, ease: [0.16, 1, 0.3, 1] }}
        className="text-center mb-16 max-w-4xl mx-auto"
      >
        <h1
          className="font-heading font-bold text-bone uppercase leading-[0.85] tracking-[-0.06em]"
          style={{ fontSize: "clamp(3.5rem, 12vw, 9rem)" }}
        >
          Food
          <br />
          <span className="text-muted">or</span>
          <br />
          Trash
        </h1>

        <motion.p
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          transition={{ delay: 0.4, duration: 0.6 }}
          className="mt-8 text-sm sm:text-base text-bone/90 font-body max-w-lg mx-auto leading-relaxed uppercase tracking-[0.15em]"
        >
          AI<span className="lowercase">s</span> and dieticians are trained on biased information.
          <br />
          Real food is what we evolved to eat.
        </motion.p>

        <motion.p
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          transition={{ delay: 0.6, duration: 0.6 }}
          className="mt-4 text-xs text-bone/60 font-body uppercase tracking-[0.2em]"
        >
          Whole foods are food &middot; Seed oils are trash &middot; Processed
          is not food
        </motion.p>
      </motion.div>

      {/* Checker */}
      <motion.div
        initial={{ opacity: 0, y: 30 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ delay: 0.3, duration: 0.7, ease: [0.16, 1, 0.3, 1] }}
        className="w-full"
      >
        <FoodChecker />
      </motion.div>

      {/* Ad slot — below verdict area */}
      <div className="w-full max-w-xl mx-auto mt-12 px-4">
        <div
          id="ad-container"
          className="min-h-[90px] flex items-center justify-center border border-border/10"
        >
          {/*
            AdSense placeholder — replace with your ad unit:
            <ins className="adsbygoogle"
              style={{ display: "block" }}
              data-ad-client="ca-pub-XXXXXXXXXXXXXXXX"
              data-ad-slot="XXXXXXXXXX"
              data-ad-format="auto"
              data-full-width-responsive="true" />
          */}
          <span className="text-[9px] text-muted/20 uppercase tracking-[0.2em]">ad</span>
        </div>
      </div>

      {/* Footer */}
      <footer className="mt-auto pt-20 pb-8 text-center space-y-4">
        {/* Ko-fi */}
        <a
          href="https://ko-fi.com/YOUR_KOFI_USERNAME"
          target="_blank"
          rel="noopener noreferrer"
          className="inline-block px-5 py-2 text-[10px] font-body text-muted/40 uppercase tracking-[0.25em] border border-border hover:border-bone/20 hover:text-muted transition-all"
        >
          Support this project
        </a>
        <p className="text-[10px] text-muted/30 font-body uppercase tracking-[0.3em]">
          foodortrash.com &mdash; no seed oils &middot; no bias &middot; just
          truth
        </p>
      </footer>
    </main>
    </>
  );
}
