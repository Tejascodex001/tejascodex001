"""Generates the profile SVGs in assets/ (dark and light variants).

Run from the repo root:  python3 assets/src/build.py
Fonts are embedded as base64 so they render inside <img> on GitHub.
"""
import base64
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parent
OUT = ROOT.parent

THEMES = {
    "dark": dict(bg="#0d1117", panel="#11161e", line="#232a35", text="#e6edf3",
                 muted="#8b949e", faint="#30363d", accent="#ff8a3d", accent2="#7aa2f7"),
    "light": dict(bg="#ffffff", panel="#fafbfc", line="#d8dee4", text="#1f2328",
                  muted="#59636e", faint="#d0d7de", accent="#d4570f", accent2="#3a63c9"),
}


def font(name, family, style="normal", weight=400):
    data = base64.b64encode((ROOT / "fonts" / f"{name}.woff2").read_bytes()).decode()
    return (f"@font-face{{font-family:'{family}';font-style:{style};font-weight:{weight};"
            f"src:url(data:font/woff2;base64,{data}) format('woff2')}}")


def fonts(*names):
    table = {
        "serif": ("InstrumentSerif-400", "Serif"),
        "serif-i": ("InstrumentSerif-400-italic", "Serif", "italic"),
        "sans": ("Figtree-400", "Sans"),
        "sans-m": ("Figtree-500", "Sans", "normal", 500),
        "mono": ("JetBrainsMono-500", "Mono", "normal", 500),
    }
    return "".join(font(*table[n]) for n in names)


BASE_CSS = """
.serif{font-family:'Serif',Georgia,serif}
.sans{font-family:'Sans',system-ui,sans-serif}
.mono{font-family:'Mono',ui-monospace,monospace;letter-spacing:.12em}
.in{opacity:0;animation:in .9s cubic-bezier(.2,.7,.2,1) forwards}
@keyframes in{from{opacity:0;transform:translateY(14px)}to{opacity:1;transform:none}}
"""


def loss_curve(x0, y0, w, h, n=90):
    """A plausible training-loss curve: fast decay, gentle noise, flattening out."""
    pts = []
    for i in range(n + 1):
        t = i / n
        v = 0.12 + 0.88 * math.exp(-5.2 * t)
        v += 0.035 * math.sin(i * 1.7) * math.exp(-2.5 * t) + 0.012 * math.sin(i * 4.3)
        pts.append((x0 + t * w, y0 + (1 - v) * h))
    return "M" + " L".join(f"{x:.1f} {y:.1f}" for x, y in pts), pts[-1]


def hero(c):
    path, (ex, ey) = loss_curve(800, 120, 330, 220)
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="440" viewBox="0 0 1200 440">
<style>{fonts('serif', 'serif-i', 'sans', 'mono')}{BASE_CSS}
.curve{{stroke-dasharray:1400;stroke-dashoffset:1400;animation:draw 9s cubic-bezier(.3,.6,.3,1) 1s infinite}}
@keyframes draw{{0%{{stroke-dashoffset:1400;opacity:1}}45%{{stroke-dashoffset:0}}88%{{stroke-dashoffset:0;opacity:1}}100%{{stroke-dashoffset:0;opacity:0}}}}
.glow{{animation:pulse 2.4s ease-in-out infinite}}
@keyframes pulse{{50%{{opacity:.25}}}}
</style>
<rect width="1200" height="440" fill="{c['bg']}"/>
<g class="in" style="animation-delay:.1s"><text x="64" y="92" class="mono" font-size="15" fill="{c['accent']}">JUNIOR AI ENGINEER  ·  KENPATH</text></g>
<g class="in" style="animation-delay:.25s"><text x="58" y="208" class="serif" font-size="124" fill="{c['text']}">Tejas Gowda <tspan font-style="italic" fill="{c['accent']}">S</tspan></text></g>
<g class="in" style="animation-delay:.45s" font-size="26" fill="{c['muted']}">
<text x="64" y="272" class="sans">I train language models from scratch, build private</text>
<text x="64" y="308" class="sans">software, and write code that runs close to the metal.</text></g>
<g class="in" style="animation-delay:.65s"><text x="64" y="378" class="mono" font-size="13" fill="{c['muted']}">BANGALORE, INDIA   ·   B.E. AI &amp; DATA SCIENCE, 2026</text></g>

<g class="in" style="animation-delay:.6s">
<text x="800" y="92" class="mono" font-size="12" fill="{c['muted']}">flame train  --run tinystories-5m</text>
<path d="M800 120 V340 H1130" fill="none" stroke="{c['faint']}" stroke-width="1"/>
<path d="M800 {ey:.1f} H1130" stroke="{c['faint']}" stroke-dasharray="3 5"/>
<text x="800" y="112" class="mono" font-size="11" fill="{c['muted']}">loss</text>
<text x="1130" y="362" class="mono" font-size="11" fill="{c['muted']}" text-anchor="end">step</text>
<path class="curve" d="{path}" fill="none" stroke="{c['accent']}" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/>
<circle class="glow" cx="{ex:.1f}" cy="{ey:.1f}" r="4" fill="{c['accent']}"/>
</g>
</svg>"""


def card(c, num, label, title, lines, stack, visual):
    desc = "".join(f'<text x="40" y="{176 + i * 29}" class="sans">{l}</text>' for i, l in enumerate(lines))
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="600" height="340" viewBox="0 0 600 340">
<style>{fonts('serif', 'sans', 'mono')}{BASE_CSS}{visual[0]}</style>
<rect x=".5" y=".5" width="599" height="339" rx="18" fill="{c['panel']}" stroke="{c['line']}"/>
<g class="in"><text x="40" y="56" class="mono" font-size="12" fill="{c['accent']}">{num}  /  {label}</text></g>
<g class="in" style="animation-delay:.15s"><text x="37" y="128" class="serif" font-size="66" fill="{c['text']}">{title}</text></g>
<g class="in" style="animation-delay:.3s" font-size="18.5" fill="{c['muted']}">{desc}</g>
<path d="M40 284 H560" stroke="{c['line']}"/>
<text x="40" y="312" class="mono" font-size="12" fill="{c['muted']}">{stack}</text>
<text x="560" y="312" class="mono" font-size="12" fill="{c['text']}" text-anchor="end">OPEN ↗</text>
{visual[1]}
</svg>"""


def flame_visual(c):
    """Attention: the newest token attends back over the sequence, one head at a time."""
    xs = [372 + i * 32 for i in range(6)]
    toks = "".join(f'<rect x="{x - 11}" y="122" width="22" height="22" rx="5" fill="none" stroke="{c["muted"]}" stroke-width="1.2"/>' for x in xs)
    last = xs[-1]
    arcs = ""
    for i, x in enumerate(xs[:-1]):
        r = (last - x) / 2
        arcs += (f'<path class="att" style="animation-delay:{i * .35:.2f}s" d="M{x} 118 A{r} {r * .62:.1f} 0 0 1 {last} 118" '
                 f'fill="none" stroke="{c["accent"]}" stroke-width="1.6"/>')
    css = ".att{opacity:.12;animation:att 3.5s ease-in-out infinite}@keyframes att{15%{opacity:1}45%{opacity:.12}}"
    head = f'<rect x="{last - 11}" y="122" width="22" height="22" rx="5" fill="{c["accent"]}"/>'
    return css, f'<g transform="translate(0,-30)">{arcs}{toks}{head}</g>'


def sanctum_visual(c):
    """A sigil: two counter-rotating star polygons, like the per-chat artwork in the app."""
    def star(n, k, r):
        pts = [(r * math.sin(2 * math.pi * i * k / n), -r * math.cos(2 * math.pi * i * k / n)) for i in range(n)]
        return "M" + " L".join(f"{x:.1f} {y:.1f}" for x, y in pts) + "Z"
    css = ""
    spin = '<animateTransform attributeName="transform" type="rotate" from="0" to="{}" dur="{}s" repeatCount="indefinite"/>' 
    g = (f'<g transform="translate(486 92)">'
         f'<circle r="54" fill="none" stroke="{c["faint"]}"/>'
         f'<g><path d="{star(7, 3, 50)}" fill="none" stroke="{c["accent"]}" stroke-width="1.4"/>{spin.format(360, 40)}</g>'
         f'<g><path d="{star(5, 2, 30)}" fill="none" stroke="{c["accent2"]}" stroke-width="1.4"/>{spin.format(-360, 60)}</g>'
         f'<circle r="3.5" fill="{c["text"]}"/></g>')
    return css, g


for name, c in THEMES.items():
    (OUT / f"hero-{name}.svg").write_text(hero(c))
    (OUT / f"flame-{name}.svg").write_text(card(
        c, "01", "LANGUAGE MODELS", "FLAME",
        ["A Rust + Candle framework for training language",
         "models from scratch on a single laptop. The base",
         "for FLAME-Research and Lintless, a Rust error fixer."],
        "RUST · CANDLE · CUDA", flame_visual(c)))
    (OUT / f"sanctum-{name}.svg").write_text(card(
        c, "02", "PRIVATE MESSAGING", "Sanctum",
        ["A peer-to-peer messenger for close friends. No",
         "servers, no accounts: end-to-end encrypted with",
         "MLS and routed over Tor. Android, now in beta."],
        "RUST · FLUTTER · TOR · MLS", sanctum_visual(c)))
