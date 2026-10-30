"""Generates assets/metrics-{dark,light}.svg from live GitHub data.

Run by .github/workflows/metrics.yml every day. Locally:
    GITHUB_TOKEN=... python3 assets/src/metrics.py
    python3 assets/src/metrics.py --sample      # fake data, for previewing the design
"""
import json
import os
import random
import sys
import urllib.request
from datetime import date, timedelta

from build import BASE_CSS, OUT, THEMES, fonts

USER = "Tejascodex001"
QUERY = """
query($login: String!) {
  user(login: $login) {
    contributionsCollection {
      contributionCalendar {
        totalContributions
        weeks { contributionDays { contributionCount date } }
      }
    }
    repositories(ownerAffiliations: OWNER, isFork: false, privacy: PUBLIC, first: 100) {
      totalCount
      nodes {
        stargazerCount
        languages(first: 10, orderBy: {field: SIZE, direction: DESC}) {
          edges { size node { name } }
        }
      }
    }
  }
}
"""


def fetch():
    req = urllib.request.Request(
        "https://api.github.com/graphql",
        data=json.dumps({"query": QUERY, "variables": {"login": USER}}).encode(),
        headers={"Authorization": f"bearer {os.environ['GITHUB_TOKEN']}",
                 "Content-Type": "application/json"},
    )
    user = json.load(urllib.request.urlopen(req))["data"]["user"]
    cal = user["contributionsCollection"]["contributionCalendar"]
    repos = user["repositories"]
    langs = {}
    for r in repos["nodes"]:
        for e in r["languages"]["edges"]:
            langs[e["node"]["name"]] = langs.get(e["node"]["name"], 0) + e["size"]
    return dict(
        total=cal["totalContributions"],
        weeks=[[d["contributionCount"] for d in w["contributionDays"]] for w in cal["weeks"]],
        repos=repos["totalCount"],
        stars=sum(r["stargazerCount"] for r in repos["nodes"]),
        langs=langs,
    )


def sample():
    rnd = random.Random(7)
    weeks = [[max(0, int(rnd.gauss(3, 4))) if rnd.random() > .35 else 0 for _ in range(7)] for _ in range(53)]
    return dict(total=sum(map(sum, weeks)), weeks=weeks, repos=18, stars=12,
                langs={"Rust": 900, "Python": 700, "C++": 300, "Dart": 200, "HTML": 90, "Shell": 20})


def streak(weeks):
    """Longest run of consecutive days with at least one contribution."""
    best = run = 0
    for count in (c for w in weeks for c in w):
        run = run + 1 if count else 0
        best = max(best, run)
    return best


def render(c, m):
    # Headline numbers
    stats = [(f"{m['total']:,}", "CONTRIBUTIONS · 1 YR"), (str(streak(m["weeks"])), "LONGEST STREAK · DAYS"),
             (str(m["repos"]), "PUBLIC REPOS"), (str(m["stars"]), "STARS")]
    nums = "".join(
        f'<g class="in" style="animation-delay:{.1 + i * .1:.1f}s">'
        f'<text x="{64 + i * 196}" y="112" class="serif" font-size="58" fill="{c["text"]}">{v}</text>'
        f'<text x="{66 + i * 196}" y="140" class="mono" font-size="11" fill="{c["muted"]}">{label}</text></g>'
        for i, (v, label) in enumerate(stats))

    # Languages: one stacked bar plus a legend, top five
    top = sorted(m["langs"].items(), key=lambda kv: -kv[1])[:5]
    total = sum(v for _, v in top) or 1
    shades = [1, .72, .5, .34, .2]
    bar, legend, x = "", "", 900.0
    for i, (name, v) in enumerate(top):
        w = 236 * v / total
        bar += f'<rect x="{x:.1f}" y="64" width="{max(w - 2, 1):.1f}" height="8" fill="{c["accent"]}" fill-opacity="{shades[i]}"/>'
        x += w
        y = 98 + i * 19
        legend += (f'<rect x="900" y="{y - 8}" width="8" height="8" fill="{c["accent"]}" fill-opacity="{shades[i]}"/>'
                   f'<text x="916" y="{y}" class="mono" font-size="11" fill="{c["text"]}">{name.upper()}</text>'
                   f'<text x="1136" y="{y}" class="mono" font-size="11" fill="{c["muted"]}" text-anchor="end">{100 * v / total:.0f}%</text>')
    langs = (f'<g class="in" style="animation-delay:.5s"><text x="900" y="48" class="mono" font-size="11" fill="{c["muted"]}">LANGUAGES</text>'
             f'<clipPath id="r"><rect x="900" y="64" width="236" height="8" rx="4"/></clipPath><g clip-path="url(#r)">{bar}</g>{legend}</g>')

    # Heatmap: last 53 weeks, levels from quartiles of active days
    active = sorted(c_ for w in m["weeks"] for c_ in w if c_)
    q = [active[int(len(active) * f)] for f in (.25, .5, .75)] if active else [1, 2, 3]
    cells = ""
    weeks = m["weeks"][-53:]
    for wi, week in enumerate(weeks):
        for di, n in enumerate(week):
            lvl = 0 if n == 0 else 1 + sum(n > t for t in q)
            fill = (f'fill="{c["faint"]}" fill-opacity=".45"' if lvl == 0
                    else f'fill="{c["accent"]}" fill-opacity="{[.3, .5, .75, 1][lvl - 1]}"')
            cells += (f'<rect class="cell" style="animation-delay:{.6 + wi * .018:.3f}s" x="{64 + wi * 20}" '
                      f'y="{216 + di * 20}" width="16" height="16" rx="3.5" {fill}/>')
    months = ""
    start = date.today() - timedelta(weeks=len(weeks) - 1)
    for wi in range(1, len(weeks) - 2):
        d = start + timedelta(weeks=wi)
        if d.month != (d - timedelta(weeks=1)).month:
            months += f'<text x="{64 + wi * 20}" y="202" class="mono" font-size="11" fill="{c["muted"]}">{d.strftime("%b").upper()}</text>'

    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="396" viewBox="0 0 1200 396">
<style>{fonts('serif', 'mono')}{BASE_CSS}
.cell{{opacity:0;animation:pop .5s ease-out forwards}}
@keyframes pop{{from{{opacity:0}}to{{opacity:1}}}}
</style>
<rect x=".5" y=".5" width="1199" height="395" rx="18" fill="{c['panel']}" stroke="{c['line']}"/>
<text x="64" y="48" class="mono" font-size="12" fill="{c['accent']}">03  /  ACTIVITY</text>
{nums}{langs}{months}{cells}
</svg>"""


def main():
    m = sample() if "--sample" in sys.argv else fetch()
    for name, c in THEMES.items():
        (OUT / f"metrics-{name}.svg").write_text(render(c, m))


if __name__ == "__main__":
    main()
