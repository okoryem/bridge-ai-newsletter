"""Download every Bridge AI newsletter issue from Substack as plain text."""
import json, re, sys, urllib.request
from html.parser import HTMLParser
from pathlib import Path

BASE = "https://deanmazlish52.substack.com/api/v1"
OUT = Path(sys.argv[1])

def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (newsletter-eval)"})
    return json.load(urllib.request.urlopen(req, timeout=30))

class ToText(HTMLParser):
    """Turn post HTML into simple markdown-ish text."""
    def __init__(self):
        super().__init__(); self.out = []; self.href = None
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag in ("h1", "h2"): self.out.append("\n\n## ")
        elif tag in ("h3", "h4"): self.out.append("\n\n### ")
        elif tag == "p": self.out.append("\n\n")
        elif tag == "li": self.out.append("\n- ")
        elif tag in ("strong", "b"): self.out.append("**")
        elif tag in ("em", "i"): self.out.append("_")
        elif tag == "br": self.out.append("\n")
        elif tag == "a": self.href = a.get("href"); self.out.append("[")
    def handle_endtag(self, tag):
        if tag in ("strong", "b"): self.out.append("**")
        elif tag in ("em", "i"): self.out.append("_")
        elif tag == "a": self.out.append(f"]({self.href})" if self.href else "]")
    def handle_data(self, data): self.out.append(data)
    def text(self):
        t = "".join(self.out)
        return re.sub(r"\n{3,}", "\n\n", t).strip()

SLUGS = [
    "every-booth-on-the-floor-was-selling", "the-white-house-forgot-one-sentence",
    "lucky-number-7", "keynes-promised-us-a-15-hour-week", "anthropic-loses-money-on-its-best",
    "is-that-a-teletubby", "ms-frizzle-takes-on-the-black-box", "everybody-building-this-thinks-it",
    "the-amazon-let-me-forget-about-ai", "life-ai-and-a-wedding-in-ecuador", "the-permission-slip",
    "claude-now-watermarks-everything",
]
posts = [{"slug": s} for s in SLUGS]
for meta in posts:
    post = get(f"{BASE}/posts/{meta['slug']}")
    p = ToText(); p.feed(post.get("body_html") or "")
    date = post["post_date"][:10]
    header = f"# {post['title']}\n"
    if post.get("subtitle"): header += f"_{post['subtitle']}_\n"
    header += f"Date: {date}\n"
    path = OUT / f"{date}_{meta['slug']}.md"
    path.write_text(header + "\n" + p.text() + "\n")
    print(path.name, len(p.text().split()), "words")
