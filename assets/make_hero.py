"""Generates the light and dark hero banners for the profile README.

Run: python3 assets/make_hero.py
"""
from pathlib import Path

THEMES = {
    "dark": dict(bg="#0B0D12", grid="#161A23", ink="#F2F4F8", muted="#8B93A7",
                 accent="#7C9CFF", accent2="#C08CFF", dot="#2A3040"),
    "light": dict(bg="#FAFAFB", grid="#ECEEF3", ink="#11131A", muted="#5B6275",
                  accent="#3B5BDB", accent2="#8B3FD9", dot="#D5D9E2"),
}

W, H = 1200, 340


def svg(t):
    grid = "".join(
        f'<line x1="{x}" y1="0" x2="{x}" y2="{H}" />' for x in range(0, W + 1, 40)
    ) + "".join(
        f'<line x1="0" y1="{y}" x2="{W}" y2="{y}" />' for y in range(0, H + 1, 40)
    )
    # A small constellation on the right: the projects as nodes, wired together.
    nodes = [(905, 92), (985, 70), (1060, 118), (1120, 84), (1010, 168),
             (1095, 210), (940, 230), (1030, 262), (1150, 170)]
    edges = [(0, 1), (1, 2), (2, 3), (1, 4), (2, 4), (4, 5), (4, 6), (6, 7),
             (5, 7), (3, 8), (5, 8)]
    lines = "".join(
        f'<line x1="{nodes[a][0]}" y1="{nodes[a][1]}" x2="{nodes[b][0]}" y2="{nodes[b][1]}" />'
        for a, b in edges
    )
    dots = "".join(
        f'<circle cx="{x}" cy="{y}" r="{5 if i in (1, 4, 5) else 3.5}" '
        f'class="n" style="animation-delay:{i * 0.35:.2f}s" />'
        for i, (x, y) in enumerate(nodes)
    )
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="Bogdan Ljubinković. Software engineering student in Novi Sad. Building things worth using with people worth building with.">
  <defs>
    <linearGradient id="g" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="{t['accent']}" />
      <stop offset="1" stop-color="{t['accent2']}" />
    </linearGradient>
    <radialGradient id="glow" cx="0.82" cy="0.45" r="0.45">
      <stop offset="0" stop-color="{t['accent']}" stop-opacity="0.16" />
      <stop offset="1" stop-color="{t['accent']}" stop-opacity="0" />
    </radialGradient>
    <linearGradient id="fade" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="{t['bg']}" stop-opacity="1" />
      <stop offset="0.55" stop-color="{t['bg']}" stop-opacity="0.6" />
      <stop offset="1" stop-color="{t['bg']}" stop-opacity="0" />
    </linearGradient>
    <clipPath id="r"><rect width="{W}" height="{H}" rx="18" /></clipPath>
    <style>
      .sans {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Inter, Helvetica, Arial, sans-serif; }}
      .mono {{ font-family: ui-monospace, SFMono-Regular, "JetBrains Mono", Menlo, Consolas, monospace; }}
      .n {{ fill: {t['accent']}; animation: pulse 3.2s ease-in-out infinite; }}
      .cur {{ animation: blink 1.1s steps(1) infinite; }}
      @keyframes pulse {{ 0%,100% {{ opacity: .35 }} 50% {{ opacity: 1 }} }}
      @keyframes blink {{ 50% {{ opacity: 0 }} }}
      @media (prefers-reduced-motion: reduce) {{ .n, .cur {{ animation: none; }} }}
    </style>
  </defs>
  <g clip-path="url(#r)">
    <rect width="{W}" height="{H}" fill="{t['bg']}" />
    <g stroke="{t['grid']}" stroke-width="1">{grid}</g>
    <rect width="{W}" height="{H}" fill="url(#glow)" />
    <rect width="760" height="{H}" fill="url(#fade)" />
    <g stroke="{t['dot']}" stroke-width="1.2">{lines}</g>
    {dots}

    <text x="64" y="86" class="mono" font-size="17" fill="{t['muted']}">
      <tspan fill="{t['accent']}">~/novi-sad</tspan> $ whoami<tspan class="cur" fill="{t['accent']}"> ▍</tspan>
    </text>
    <text x="62" y="168" class="sans" font-size="68" font-weight="800" letter-spacing="-2" fill="{t['ink']}">Bogdan Ljubinković</text>
    <rect x="64" y="192" width="132" height="5" rx="2.5" fill="url(#g)" />
    <text x="64" y="240" class="sans" font-size="24" font-weight="500" fill="{t['ink']}">Building things worth using</text>
    <text x="64" y="272" class="sans" font-size="24" font-weight="500" fill="{t['muted']}">with people worth building with.</text>
  </g>
</svg>
'''


out = Path(__file__).parent
for name, theme in THEMES.items():
    (out / f"hero-{name}.svg").write_text(svg(theme), encoding="utf-8")
print("wrote", ", ".join(f"hero-{n}.svg" for n in THEMES))
