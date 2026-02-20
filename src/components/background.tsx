"use client";

import { useEffect, useState } from "react";
import Image from "next/image";
import { motion } from "framer-motion";

const images = [
  "/images/bg1.webp",
  "/images/bg2.webp",
  "/images/bg3.webp",
  "/images/bg4.webp",
  "/images/bg5.webp",
  "/images/bg6.webp",
];

// Each fragment: position, size, rotation, opacity, drift direction
const fragments = [
  { x: "5%", y: "8%", w: 280, h: 200, rot: -4, opacity: 0.22, driftX: 15, driftY: -10, img: 0 },
  { x: "65%", y: "5%", w: 220, h: 160, rot: 2.5, opacity: 0.14, driftX: -10, driftY: 12, img: 1 },
  { x: "80%", y: "55%", w: 260, h: 180, rot: -1.5, opacity: 0.18, driftX: -12, driftY: -8, img: 2 },
  { x: "2%", y: "60%", w: 200, h: 150, rot: 3, opacity: 0.12, driftX: 8, driftY: 15, img: 3 },
  { x: "35%", y: "75%", w: 240, h: 170, rot: -2, opacity: 0.16, driftX: -15, driftY: -12, img: 4 },
  { x: "50%", y: "25%", w: 180, h: 130, rot: 1, opacity: 0.1, driftX: 10, driftY: 8, img: 5 },
  { x: "20%", y: "35%", w: 160, h: 120, rot: -3.5, opacity: 0.08, driftX: -8, driftY: -15, img: 0 },
  { x: "75%", y: "80%", w: 200, h: 140, rot: 2, opacity: 0.13, driftX: 12, driftY: -10, img: 2 },
];

export function Background() {
  const [mounted, setMounted] = useState(false);

  useEffect(() => {
    setMounted(true);
  }, []);

  if (!mounted) return <div className="fixed inset-0 -z-10 bg-void" />;

  return (
    <div className="fixed inset-0 -z-10 overflow-hidden">
      <div className="absolute inset-0 bg-void" />

      {fragments.map((frag, i) => (
        <motion.div
          key={i}
          className="absolute"
          style={{
            left: frag.x,
            top: frag.y,
            width: frag.w,
            height: frag.h,
          }}
          initial={{
            rotate: frag.rot,
            opacity: 0,
          }}
          animate={{
            rotate: frag.rot,
            opacity: frag.opacity,
            x: [0, frag.driftX, 0],
            y: [0, frag.driftY, 0],
          }}
          transition={{
            opacity: { duration: 2, delay: i * 0.3 },
            x: {
              duration: 20 + i * 3,
              repeat: Infinity,
              repeatType: "reverse",
              ease: "easeInOut",
            },
            y: {
              duration: 25 + i * 2,
              repeat: Infinity,
              repeatType: "reverse",
              ease: "easeInOut",
            },
          }}
        >
          <Image
            src={images[frag.img]}
            alt=""
            fill
            className="object-cover"
            sizes={`${frag.w}px`}
          />
        </motion.div>
      ))}

      {/* Grain texture */}
      <div
        className="absolute inset-0 opacity-[0.04] pointer-events-none"
        style={{
          backgroundImage: `url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)' opacity='1'/%3E%3C/svg%3E")`,
          backgroundRepeat: "repeat",
          backgroundSize: "128px 128px",
        }}
      />
    </div>
  );
}
