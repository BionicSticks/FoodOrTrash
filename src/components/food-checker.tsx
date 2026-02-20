"use client";

import { useState, useCallback, useEffect } from "react";
import { motion } from "framer-motion";
import { lookupFood } from "@/lib/food-lookup";
import type { LookupResult } from "@/lib/foods";
import { Verdict } from "./verdict";
import { SearchHistory } from "./search-history";
import { ShareButton } from "./share-button";

interface HistoryEntry {
  query: string;
  result: LookupResult;
  timestamp: number;
}

export function FoodChecker() {
  const [query, setQuery] = useState("");
  const [result, setResult] = useState<LookupResult | null>(null);
  const [currentQuery, setCurrentQuery] = useState("");
  const [loading, setLoading] = useState(false);
  const [history, setHistory] = useState<HistoryEntry[]>([]);

  // Load history from localStorage after mount (avoids hydration mismatch)
  useEffect(() => {
    try {
      const stored = localStorage.getItem("foodortrash-history");
      if (stored) setHistory(JSON.parse(stored));
    } catch {
      // localStorage unavailable
    }
  }, []);

  const saveHistory = useCallback(
    (entries: HistoryEntry[]) => {
      setHistory(entries);
      try {
        localStorage.setItem("foodortrash-history", JSON.stringify(entries));
      } catch {
        // localStorage full or unavailable
      }
    },
    []
  );

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    const trimmed = query.trim();
    if (!trimmed) return;

    setCurrentQuery(trimmed);
    setResult(null);

    // Try local lookup first
    const localResult = lookupFood(trimmed);
    if (localResult) {
      setResult(localResult);
      const entry: HistoryEntry = {
        query: trimmed,
        result: localResult,
        timestamp: Date.now(),
      };
      saveHistory([entry, ...history].slice(0, 50));
      setQuery("");
      return;
    }

    // Fall back to AI
    setLoading(true);
    try {
      const res = await fetch("/api/check", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ item: trimmed }),
      });
      const data = await res.json();
      const aiResult: LookupResult = {
        found: data.isFood,
        source: "ai",
        verdict: data.isFood ? "food" : "trash",
        aiReason: data.reason,
      };
      setResult(aiResult);
      const entry: HistoryEntry = {
        query: trimmed,
        result: aiResult,
        timestamp: Date.now(),
      };
      saveHistory([entry, ...history].slice(0, 50));
    } catch {
      const fallback: LookupResult = {
        found: false,
        source: "ai",
        verdict: "trash",
        aiReason: "Couldn't verify this one. When in doubt... trash.",
      };
      setResult(fallback);
    } finally {
      setLoading(false);
      setQuery("");
    }
  };

  const clearHistory = () => {
    saveHistory([]);
  };

  return (
    <div className="w-full max-w-xl mx-auto px-4">
      {/* Input form */}
      <form onSubmit={handleSubmit}>
        <div className="flex gap-3">
          <input
            type="text"
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            placeholder="TYPE ANYTHING..."
            className="flex-1 px-6 py-4 rounded-none bg-surface border border-border text-bone text-base sm:text-lg font-body uppercase tracking-[0.1em] placeholder:text-muted/30 placeholder:uppercase focus:outline-none focus:border-bone/30 transition-colors"
            disabled={loading}
            autoFocus
          />
          <motion.button
            type="submit"
            disabled={loading || !query.trim()}
            whileHover={{ scale: 1.02 }}
            whileTap={{ scale: 0.98 }}
            className="px-8 py-4 rounded-none bg-bone text-void font-heading font-bold text-base uppercase tracking-[0.15em] disabled:opacity-20 disabled:cursor-not-allowed transition-all hover:bg-bone/90"
          >
            {loading ? (
              <motion.span
                animate={{ opacity: [1, 0.3, 1] }}
                transition={{ repeat: Infinity, duration: 1 }}
              >
                ...
              </motion.span>
            ) : (
              "Judge"
            )}
          </motion.button>
        </div>
      </form>

      {/* Loading state */}
      {loading && (
        <motion.p
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          className="text-center text-muted/50 mt-8 text-xs font-body uppercase tracking-[0.2em]"
        >
          Consulting the oracle...
        </motion.p>
      )}

      {/* Verdict */}
      <Verdict result={result} query={currentQuery} />

      {/* Share button */}
      {result && <ShareButton query={currentQuery} result={result} />}

      {/* History */}
      {history.length > 0 && (
        <SearchHistory entries={history} onClear={clearHistory} />
      )}
    </div>
  );
}
