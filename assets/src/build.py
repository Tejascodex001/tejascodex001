"""Build GitHub-compatible animated SVGs and still variants for both READMEs.

Run: python3 assets/src/build.py [--org-output PATH/TO/.github/profile/assets]
Fonts are embedded; images use native SVG animation without JavaScript or remote
requests. README <picture> sources select still artwork for reduced motion.
"""
import argparse
import base64
import html
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parent
OUT = ROOT.parent
THEMES = {
    'dark': dict(bg='#0d1117', panel='#131922', line='#2b3442', text='#f3f0e9',
                 muted='#a8b1bd', accent='#ecc574', cyan='#8fd6df', violet='#b8a0e1'),
    'light': dict(bg='#faf8f3', panel='#fffdf9', line='#d8d9d7', text='#252a31',
                  muted='#596775', accent='#8d6021', cyan='#286d7d', violet='#71539c'),
}


def font_styles():
    result = []
    for name, family in [('Figtree-500', 'Sans'), ('InstrumentSerif-400', 'Serif')]:
        data = base64.b64encode((ROOT / 'fonts' / (name + '.woff2')).read_bytes()).decode()
        result.append("@font-face{font-family:'" + family + "';src:url(data:font/woff2;base64," + data + ") format('woff2')}")
    result.append(".sans{font-family:'Sans',system-ui,sans-serif}.serif{font-family:'Serif',Georgia,serif}text{font-weight:400}")
    return ''.join(result)


def anim(attribute, values, duration=6, begin=0, still=False):
    if still:
        return ''
    return f'<animate attributeName="{attribute}" values="{values}" dur="{duration}s" begin="{begin}s" repeatCount="indefinite"/>'


def rotate(duration, reverse=False, still=False):
    if still:
        return ''
    return f'<animateTransform attributeName="transform" type="rotate" from="0" to="{-360 if reverse else 360}" dur="{duration}s" repeatCount="indefinite"/>'


def packet(path, x, y, color, duration=6, begin=0, still=False):
    if still:
        return f'<circle cx="{x}" cy="{y}" r="3.2" fill="{color}"/>'
    return f'<circle r="3.2" fill="{color}"><animateMotion path="{path}" dur="{duration}s" begin="{begin}s" repeatCount="indefinite"/></circle>'


def text(x, y, content, size, color, family='sans', extra=''):
    return f'<text x="{x}" y="{y}" class="{family}" font-size="{size}" fill="{color}" {extra}>{html.escape(content)}</text>'


def svg(body, title, height=340):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="900" height="{height}" viewBox="0 0 900 {height}" role="img">'
            f'<title>{html.escape(title)}</title><style>{font_styles()}</style>{body}</svg>\n')


def frame(c, height=340):
    result = [f'<rect x=".5" y=".5" width="899" height="{height - 1}" rx="24" fill="{c["bg"]}" stroke="{c["line"]}"/>']
    for x in range(570, 901, 30):
        result.append(f'<path d="M{x} 1V{height - 1}" stroke="{c["line"]}" opacity=".25"/>')
    for y in range(20, height, 30):
        result.append(f'<path d="M570 {y}H899" stroke="{c["line"]}" opacity=".25"/>')
    return ''.join(result)


def constellation(c, still=False, x=733, y=170, radius=117):
    out = [f'<g transform="translate({x} {y})">']
    for index in range(3):
        angle = 20 + index * 57
        out.append(f'<g transform="rotate({angle})"><ellipse rx="{radius}" ry="{radius * .42}" fill="none" stroke="{c["line"]}" stroke-width="1.2"/></g>')
    for index in range(2):
        out.append('<g>')
        points = []
        count = 7 + index * 2
        r = radius * (1 - index * .29)
        for i in range(count):
            angle = math.tau * i / count - math.pi / 2
            points.append((r * math.cos(angle), r * math.sin(angle)))
        for i, (px, py) in enumerate(points):
            nx, ny = points[(i + 2) % count]
            color = c['accent'] if index == 0 else c['cyan']
            out.append(f'<path d="M{px:.2f} {py:.2f}L{nx:.2f} {ny:.2f}" stroke="{color}" fill="none" opacity=".3"/>')
            out.append(f'<circle cx="{px:.2f}" cy="{py:.2f}" r="3.5" fill="{color}">')
            out.append(anim('opacity', '.35;1;.35', 4 + i % 3, -i * .7, still))
            out.append('</circle>')
        out.append(rotate(42 if index == 0 else 30, reverse=index == 1, still=still))
        out.append('</g>')
    for i in range(3):
        color = [c['cyan'], c['accent'], c['violet']][i]
        path = f'M{-radius} 0C{-radius} {-radius * .55} {radius} {-radius * .55} {radius} 0C{radius} {radius * .55} {-radius} {radius * .55} {-radius} 0'
        out.append(f'<g transform="rotate({i * 58 - 20})">')
        out.append(packet(path, -radius, 0, color, 8 + i * 2, -i * 2, still))
        out.append('</g>')
    out.append(f'<circle r="28" fill="{c["panel"]}" stroke="{c["line"]}"/>')
    out.append(f'<circle r="8" fill="{c["accent"]}">{anim("opacity", ".45;1;.45", 5, 0, still)}</circle>')
    out.append('</g>')
    return ''.join(out)


def lab(c, still=False):
    out = frame(c)
    out += text(42, 61, 'INDEPENDENT RESEARCH + ENGINEERING', 15, c['accent'], extra='letter-spacing="1.6"')
    out += text(37, 157, 'RTensorLabs', 86, c['text'], 'serif')
    out += text(42, 209, 'Explore ideas. Build useful things.', 26, c['muted'])
    out += text(42, 281, 'First principles. New questions. Open possibilities.', 17, c['muted'])
    out += constellation(c, still)
    return svg(out, 'RTensorLabs — independent research and engineering across fields')


def personal(c, still=False):
    out = frame(c)
    out += text(42, 61, 'JUNIOR AI ENGINEER / KENPATH', 16, c['accent'], extra='letter-spacing="1.5"')
    out += text(37, 157, 'Tejas Gowda S', 79, c['text'], 'serif')
    out += text(42, 210, 'Models. Systems. Software for people.', 25, c['muted'])
    out += f'<path d="M42 244H507" stroke="{c["line"]}"/>'
    out += text(42, 281, 'Building and exploring at RTensorLabs', 19, c['muted'])
    out += constellation(c, still, radius=108)
    return svg(out, 'Tejas Gowda S — AI engineer at Kenpath and maintainer of RTensorLabs')


def model(c, still=False):
    out = []
    # A token stream feeds a small attention matrix, then leaves as a signal.
    for i in range(5):
        xx = 615 + i * 43
        out.append(f'<rect x="{xx}" y="40" width="23" height="23" rx="6" fill="{c["panel"]}" stroke="{c["line"]}"/>')
        path = f'M{xx + 12} 69Q{xx + 12} 100 735 109'
        out.append(f'<path d="{path}" fill="none" stroke="{c["cyan"]}" opacity=".3"/>')
        out.append(packet(path, xx + 12, 69, c['cyan'], 3.5, -i * .6, still))
    for row in range(4):
        for col in range(5):
            opacity = .22 + ((row * 3 + col * 2) % 6) * .11
            out.append(f'<rect x="{654 + col * 32}" y="{111 + row * 23}" width="25" height="16" rx="4" fill="{c["accent"]}" opacity="{opacity:.2f}">')
            out.append(anim('opacity', f'{opacity:.2f};.95;{opacity:.2f}', 4.4, -(row + col) * .35, still))
            out.append('</rect>')
    out.append(f'<path d="M625 229H847" stroke="{c["line"]}"/>')
    path = 'M625 221C656 179 665 229 698 205S744 226 777 205S815 222 847 200'
    out.append(f'<path d="{path}" fill="none" stroke="{c["accent"]}" stroke-width="2" opacity=".6"/>')
    out.append(packet(path, 777, 205, c['accent'], 5, 0, still))
    return ''.join(out)


def friends(c, still=False):
    out = []
    for index, (x, y, color) in enumerate([(652, 94, c['cyan']), (816, 143, c['accent'])]):
        out.append(f'<g transform="translate({x} {y})"><circle r="34" fill="{c["panel"]}" stroke="{c["line"]}"/>')
        out.append('<g>')
        points = ' '.join(f'{math.cos(math.tau*i*2/7)*26:.2f},{math.sin(math.tau*i*2/7)*26:.2f}' for i in range(7))
        out.append(f'<polygon points="{points}" fill="none" stroke="{color}" stroke-width="1.7"/>')
        out.append(rotate(22 + index * 7, index == 1, still))
        out.append('</g></g>')
    path = 'M681 105C710 30 759 219 787 145'
    out.append(f'<path d="{path}" stroke="{c["line"]}" fill="none" stroke-width="1.8"/>')
    out.append(packet(path, 732, 126, c['cyan'], 4, -1, still))
    out.append(packet('M787 145C759 219 710 30 681 105', 730, 125, c['accent'], 4, -3, still))
    out.append(f'<g transform="translate(733 125)"><circle r="21" fill="{c["bg"]}" stroke="{c["line"]}"/><rect x="-8" y="-2" width="16" height="13" rx="3" fill="none" stroke="{c["text"]}" stroke-width="1.5"/><path d="M-5-2V-7a5 5 0 0 1 10 0v5" fill="none" stroke="{c["text"]}" stroke-width="1.5"/></g>')
    out.append(text(733, 226, 'YOUR PEOPLE. YOUR SPACE.', 12, c['muted'], extra='text-anchor="middle" letter-spacing="1"'))
    return ''.join(out)


def project(c, kind, still=False):
    is_model = kind == 'flame'
    title = 'FLAME' if is_model else 'Sanctum'
    eyebrow = 'LANGUAGE MODELS / FROM FIRST PRINCIPLES' if is_model else 'PRIVATE MESSAGING / ANDROID BETA'
    line = 'Understand what goes into a model.' if is_model else 'A private space for your close circle.'
    stack = 'RUST + CANDLE' if is_model else 'RUST + FLUTTER + TOR'
    out = frame(c, 270)
    out += text(34, 46, eyebrow, 12, c['accent'], extra='letter-spacing="1.4"')
    out += text(31, 124, title, 74, c['text'], 'serif')
    out += text(34, 172, line, 23, c['muted'])
    out += text(34, 232, stack, 13, c['muted'], extra='letter-spacing="1.4"')
    out += model(c, still) if is_model else friends(c, still)
    return svg(out, title + ' — ' + line, 270)


def methodology(c, still=False):
    out = f'<rect x=".5" y=".5" width="899" height="129" rx="20" fill="{c["panel"]}" stroke="{c["line"]}"/>'
    for i, label in enumerate(['EXPLORE', 'BUILD', 'SHARE']):
        x = 150 + i * 300
        out += f'<circle cx="{x}" cy="48" r="13" fill="{c["bg"]}" stroke="{c["accent"]}"/>'
        out += f'<circle cx="{x}" cy="48" r="4" fill="{c["accent"]}">{anim("opacity", ".25;1;.25", 5.5, -i*1.8, still)}</circle>'
        out += text(x, 96, label, 18, c['text'], extra='text-anchor="middle" letter-spacing="2"')
        if i < 2:
            path = f'M{x + 23} 48H{x + 277}'
            out += f'<path d="{path}" stroke="{c["line"]}" fill="none"/>'
            out += packet(path, x + 150, 48, c['cyan'], 3.8, -i * 1.5, still)
    return svg(out, 'RTensorLabs — explore, build, share', 130)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--org-output', type=Path)
    args = parser.parse_args()
    builders = {'hero-v2': personal, 'flame-v2': lambda c, s: project(c, 'flame', s),
                'sanctum-v2': lambda c, s: project(c, 'sanctum', s), 'lab-v2': lab,
                'process-v2': methodology}
    OUT.mkdir(parents=True, exist_ok=True)
    if args.org_output:
        args.org_output.mkdir(parents=True, exist_ok=True)
    for theme, colors in THEMES.items():
        for name, builder in builders.items():
            for still in [False, True]:
                filename = f'{name}-{"still-" if still else ""}{theme}.svg'
                content = builder(colors, still)
                if name not in ['lab-v2', 'process-v2']:
                    (OUT / filename).write_text(content)
                if args.org_output and name != 'hero-v2':
                    (args.org_output / filename).write_text(content)
    if args.org_output:
        for filename in ['LICENSE-figtree.txt', 'LICENSE-instrument-serif.txt']:
            (args.org_output / filename).write_text((ROOT / 'fonts' / filename).read_text())
    print('Built self-contained animated artwork and still variants.')


if __name__ == '__main__':
    main()
