"use client";

import { useState } from "react";
import { motion, AnimatePresence } from "framer-motion";
import type { LookupResult } from "@/lib/foods";

interface HistoryEntry {
  query: string;
  result: LookupResult;
  timestamp: number;
}

interface SearchHistoryProps {
  entries: HistoryEntry[];
  onClear: () => void;
}

export function SearchHistory({ entries, onClear }: SearchHistoryProps) {
  const [isOpen, setIsOpen] = useState(false);

  return (
    <motion.div
      initial={{ opacity: 0 }}
      animate={{ opacity: 1 }}
      className="mt-12 w-full max-w-xl mx-auto"
    >
      <button
        onClick={() => setIsOpen(!isOpen)}
        className="flex items-center gap-3 text-[10px] text-muted/50 hover:text-muted transition-colors font-body uppercase tracking-[0.25em]"
      >
        <motion.span
          animate={{ rotate: isOpen ? 90 : 0 }}
          transition={{ duration: 0.2 }}
          className="text-[8px]"
        >
          ▶
        </motion.span>
        History ({entries.length})
      </button>

      <AnimatePresence>
        {isOpen && (
          <motion.div
            initial={{ height: 0, opacity: 0 }}
            animate={{ height: "auto", opacity: 1 }}
            exit={{ height: 0, opacity: 0 }}
            transition={{ duration: 0.3 }}
            className="overflow-hidden"
          >
            <div className="mt-4 space-y-1 max-h-48 overflow-y-auto">
              {entries.map((entry, i) => (
                <motion.div
                  key={entry.timestamp}
                  initial={{ opacity: 0, x: -10 }}
                  animate={{ opacity: 1, x: 0 }}
                  transition={{ delay: i * 0.02 }}
                  className="flex items-center justify-between px-4 py-2.5 border border-border hover:border-border/60 transition-colors"
                >
                  <span className="text-xs text-muted font-body uppercase tracking-[0.1em]">
                    {entry.query}
                  </span>
                  <span
                    className={`text-[10px] font-bold uppercase tracking-[0.2em] ${
                      entry.result.verdict === "food"
                        ? "text-food-green"
                        : "text-trash-red"
                    }`}
                  >
                    {entry.result.verdict === "food" ? "FOOD" : "TRASH"}
                  </span>
                </motion.div>
              ))}
            </div>
            <button
              onClick={onClear}
              className="mt-3 text-[10px] text-muted/30 hover:text-trash-red transition-colors font-body uppercase tracking-[0.2em]"
            >
              Clear history
            </button>
          </motion.div>
        )}
      </AnimatePresence>
    </motion.div>
  );
}
