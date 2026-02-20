import { ImageResponse } from "next/og";
import { NextRequest } from "next/server";

export const runtime = "edge";

export async function GET(request: NextRequest) {
  const { searchParams } = request.nextUrl;
  const item = searchParams.get("item") || "something";
  const verdict = searchParams.get("verdict") || "trash";
  const category = searchParams.get("category") || "";
  const isFood = verdict === "food";

  return new ImageResponse(
    (
      <div
        style={{
          width: "100%",
          height: "100%",
          display: "flex",
          flexDirection: "column",
          alignItems: "center",
          justifyContent: "center",
          backgroundColor: "#060606",
          fontFamily: "Inter, system-ui, sans-serif",
        }}
      >
        {/* Title */}
        <div
          style={{
            fontSize: 28,
            fontWeight: 700,
            color: "#949292",
            letterSpacing: "0.2em",
            textTransform: "uppercase",
            marginBottom: 40,
          }}
        >
          FOOD OR TRASH
        </div>

        {/* Item name */}
        <div
          style={{
            fontSize: 20,
            color: "#949292",
            letterSpacing: "0.15em",
            textTransform: "uppercase",
            marginBottom: 20,
          }}
        >
          &ldquo;{item}&rdquo;
        </div>

        {/* Verdict */}
        <div
          style={{
            fontSize: 120,
            fontWeight: 900,
            color: isFood ? "#00cc66" : "#ff1a1a",
            letterSpacing: "-0.04em",
            textTransform: "uppercase",
            lineHeight: 0.85,
          }}
        >
          {isFood ? "FOOD" : "TRASH"}
        </div>

        {/* Category */}
        {isFood && category && (
          <div
            style={{
              marginTop: 30,
              padding: "8px 20px",
              fontSize: 14,
              fontWeight: 700,
              color: "#00cc66",
              letterSpacing: "0.2em",
              textTransform: "uppercase",
              border: "1px solid #00cc6644",
            }}
          >
            {category}
          </div>
        )}

        {/* URL */}
        <div
          style={{
            position: "absolute",
            bottom: 40,
            fontSize: 12,
            color: "#94929240",
            letterSpacing: "0.3em",
            textTransform: "uppercase",
          }}
        >
          foodortrash.com
        </div>
      </div>
    ),
    {
      width: 1200,
      height: 630,
    }
  );
}
