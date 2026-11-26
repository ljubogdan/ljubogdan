"""Generates the link badges under the hero banner.

They live in the repo instead of coming from shields.io, so they render
even when GitHub's image proxy can't reach an outside host.

Run: python3 assets/make_badges.py
"""
from pathlib import Path

BADGES = {
    "linkedin": ("LinkedIn", "ljubogdan", "#0A66C2"),
    "x": ("X", "@ljubogdan", "#2B303B"),
    "ordoverse": ("building", "ordoverse.com", "#5B7CFA"),
    "location": ("based in", "Novi Sad, Serbia", "#9B5DE5"),
}

LABEL_BG = "#262B36"
H = 28
PAD = 12
CHAR = 7.4  # average glyph width at 13px, generous so text never clips


def width(text):
    return round(len(text) * CHAR + 2 * PAD)


def svg(label, value, color):
    lw, vw = width(label), width(value)
    w = lw + vw
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{H}" viewBox="0 0 {w} {H}" role="img" aria-label="{label}: {value}">
  <clipPath id="c"><rect width="{w}" height="{H}" rx="6" /></clipPath>
  <g clip-path="url(#c)">
    <rect width="{lw}" height="{H}" fill="{LABEL_BG}" />
    <rect x="{lw}" width="{vw}" height="{H}" fill="{color}" />
  </g>
  <g font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Inter, Helvetica, Arial, sans-serif" font-size="13" text-anchor="middle" dominant-baseline="central">
    <text x="{lw / 2}" y="{H / 2}" fill="#C3CAD9">{label}</text>
    <text x="{lw + vw / 2}" y="{H / 2}" fill="#FFFFFF" font-weight="600">{value}</text>
  </g>
</svg>
'''


out = Path(__file__).parent
for name, (label, value, color) in BADGES.items():
    (out / f"badge-{name}.svg").write_text(svg(label, value, color), encoding="utf-8")
print("wrote", ", ".join(f"badge-{n}.svg" for n in BADGES))
