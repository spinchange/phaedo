from __future__ import annotations

import html
import re
import uuid
import zipfile
from datetime import date
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "publication"
BATCHES = sorted((ROOT / "translations").glob("batch-*.md"))
TITLE = "Phaedo"
SUBTITLE = "A New Translation"
AUTHOR = "Plato"
IDENT = "urn:uuid:" + str(uuid.uuid5(uuid.NAMESPACE_URL, "phaedo-new-translation-2026"))


def inline(text: str) -> str:
    text = html.escape(text, quote=False)
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<em>\1</em>", text)
    return text


def read_batch(path: Path) -> tuple[str, list[tuple[str, str]]]:
    raw = path.read_text(encoding="utf-8")
    body = raw.split("\n## Queries", 1)[0].strip()
    groups = re.split(r"(?m)^### (\d+[a-e])\s*$", body)
    sections: list[tuple[str, str]] = []
    for i in range(1, len(groups), 2):
        ref, content = groups[i], groups[i + 1]
        paras = []
        for para in re.split(r"\n\s*\n", content.strip()):
            p = para.strip()
            if p:
                paras.append("<p>" + inline(p) + "</p>")
        sections.append((ref, "\n".join(paras)))
    return path.stem.replace("batch-", "Part ").replace("-", " · "), sections


def xhtml(title: str, body: str, lang: str = "en") -> str:
    return (f'<?xml version="1.0" encoding="utf-8"?>\n'
            f'<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" lang="{lang}" xml:lang="{lang}">'
            f'<head><title>{html.escape(title)}</title><link rel="stylesheet" type="text/css" href="style.css" /></head>'
            f'<body>{body}</body></html>')


def main() -> None:
    OUT.mkdir(exist_ok=True)
    batches = [(path, *read_batch(path)) for path in BATCHES]
    all_sections = [(ref, content) for _, _, sections in batches for ref, content in sections]
    toc = "".join(f'<a href="#s-{ref}" data-ref="{ref}">{ref}</a>' for ref, _ in all_sections)
    html_sections = "\n".join(f'<section class="passage" id="s-{ref}"><h2>{ref}</h2>{content}</section>' for ref, content in all_sections)
    page = f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="description" content="A new modern-English translation of Plato's Phaedo, with Stephanus references.">
<meta property="og:type" content="website"><meta property="og:title" content="Phaedo: A New Translation">
<meta property="og:description" content="A new modern-English translation of Plato’s Phaedo.">
<meta property="og:url" content="https://spinchange.com/phaedo/">
<meta property="og:image" content="https://spinchange.com/phaedo/social-card.png">
<meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">
<meta property="og:image:alt" content="Phaedo — A New Translation">
<meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="Phaedo: A New Translation">
<meta name="twitter:description" content="A new modern-English translation of Plato’s Phaedo.">
<meta name="twitter:image" content="https://spinchange.com/phaedo/social-card.png">
<title>{TITLE}: {SUBTITLE}</title><style>
:root{{--ink:#202923;--muted:#627066;--paper:#fbfaf6;--green:#315b49;--line:#d9ded6;--serif:Georgia,'Times New Roman',serif}}
*{{box-sizing:border-box}}body{{margin:0;background:var(--paper);color:var(--ink);font:18px/1.75 var(--serif)}}
.mast{{background:#e9eee8;padding:64px 24px 48px;text-align:center}}.mast small{{color:var(--green);letter-spacing:.16em;text-transform:uppercase;font:600 12px system-ui}}.mast small a{{color:inherit;text-underline-offset:3px}}
h1{{font-size:clamp(44px,8vw,76px);line-height:1.05;margin:14px 0 8px;font-weight:500}}.subtitle{{font-size:22px;color:var(--muted);margin:0}}.byline{{font:14px system-ui;color:var(--muted);margin-top:24px}}
.download{{display:inline-block;margin-top:8px;padding:9px 16px;border-radius:5px;background:var(--green);color:white;text-decoration:none;font:600 14px system-ui}}.download:hover{{background:#244536}}
.cast{{max-width:760px;margin:32px auto 0;padding-top:18px;border-top:1px solid #cfd8ce}}.cast-label{{font:600 11px system-ui;letter-spacing:.14em;text-transform:uppercase;color:var(--muted)}}.cast-list{{margin:8px 0 0;color:#46534a;font:14px/1.8 system-ui}}
.layout{{max-width:1100px;margin:0 auto;padding:34px 24px;display:grid;grid-template-columns:210px minmax(0,700px);gap:56px;justify-content:center}}
aside{{position:sticky;top:20px;align-self:start;max-height:calc(100vh - 40px);overflow:auto;font:13px/1.6 system-ui}}aside h2{{font-size:12px;text-transform:uppercase;letter-spacing:.12em;color:var(--muted)}}.toc{{display:grid;grid-template-columns:repeat(4,1fr);gap:3px}}.toc a{{padding:2px 4px;color:var(--green);text-decoration:none;border-radius:3px}}.toc a:hover,.toc a.active{{background:#e5ece5}}
main{{min-width:0}}.intro{{font-size:19px;color:#46534a;margin:0 0 46px}}.passage{{scroll-margin-top:26px;border-top:1px solid var(--line);padding:24px 0 10px}}.passage h2{{font:600 14px system-ui;color:var(--green);letter-spacing:.08em;margin:0 0 12px}}p{{margin:0 0 1em}}strong{{font-weight:700}}footer{{border-top:1px solid var(--line);padding:28px 24px 46px;color:var(--muted);font:13px/1.6 system-ui;text-align:center}}
@media(max-width:740px){{.layout{{display:block;padding:22px 20px}}aside{{position:relative;top:auto;max-height:none;margin-bottom:30px}}.toc{{grid-template-columns:repeat(8,1fr)}}body{{font-size:17px}}}}
@media print{{aside,.download{{display:none}}.layout{{display:block;max-width:unset}}body{{font-size:11pt}}.passage{{break-inside:avoid}}}}
</style></head><body>
<header class="mast"><small>Plato · <a href="https://en.wikipedia.org/wiki/Stephanus_pagination" target="_blank" rel="noopener noreferrer" title="What Stephanus references mean">Stephanus</a> 57a–118a</small><h1><em>Phaedo</em></h1><p class="subtitle">A New Translation</p><p class="byline">Translated directly from the Greek · November 2, 2026</p><a class="download" href="phaedo.epub" download>Download the EPUB</a><section class="cast" aria-label="Characters"><div class="cast-label">Characters</div><p class="cast-list">Socrates · Phaedo (narrator) · Echecrates · Crito · Simmias · Cebes · Apollodorus · Xanthippe · the prison attendant</p></section></header>
<div class="layout"><aside><h2>Contents · Stephanus</h2><nav class="toc" aria-label="Stephanus sections">{toc}</nav></aside>
<main><p class="intro">Socrates’ final day, told by Phaedo: a dialogue on philosophy, the soul, and the meaning of death.</p>{html_sections}</main></div>
<footer>Translation based on the Greek text edited by John Burnet, <em>Platonis Opera</em>, vol. 1 (Oxford Classical Texts), as represented in the Perseus Digital Library. Stephanus references follow the source text. Translation project, 2026.<br>Errata and corrections: <a href="mailto:errata@spinchange.com">errata@spinchange.com</a></footer>
<script>const links=[...document.querySelectorAll('.toc a')];const obs=new IntersectionObserver(es=>es.forEach(e=>{{if(e.isIntersecting){{links.forEach(a=>a.classList.toggle('active',a.hash==='#'+e.target.id))}}}}),{{rootMargin:'-8% 0px -82% 0px'}});document.querySelectorAll('.passage').forEach(s=>obs.observe(s));</script>
</body></html>'''
    (OUT / "phaedo.html").write_text(page, encoding="utf-8")
    (OUT / "index.html").write_text(page, encoding="utf-8")
    card = Image.new("RGB", (1200, 630), "#e9eee8")
    draw = ImageDraw.Draw(card)
    draw.rounded_rectangle((42, 42, 1158, 588), radius=18, outline="#cfd8ce", width=2)
    fonts = Path("C:/Windows/Fonts")
    title_font_path = fonts / "georgiai.ttf"
    subtitle_font_path = fonts / "georgia.ttf"
    title_font = ImageFont.truetype(str(title_font_path), 112) if title_font_path.exists() else ImageFont.load_default(size=112)
    subtitle_font = ImageFont.truetype(str(subtitle_font_path), 38) if subtitle_font_path.exists() else ImageFont.load_default(size=38)
    title_text, subtitle_text, date_text = "Phaedo", "A New Translation", "November 2, 2026"
    title_box = draw.textbbox((0, 0), title_text, font=title_font)
    subtitle_box = draw.textbbox((0, 0), subtitle_text, font=subtitle_font)
    date_font_path = fonts / "arial.ttf"
    date_font = ImageFont.truetype(str(date_font_path), 23) if date_font_path.exists() else ImageFont.load_default(size=23)
    date_box = draw.textbbox((0, 0), date_text, font=date_font)
    draw.text(((1200 - (title_box[2] - title_box[0])) / 2, 228 - title_box[1]), title_text, fill="#202923", font=title_font)
    draw.text(((1200 - (subtitle_box[2] - subtitle_box[0])) / 2, 370 - subtitle_box[1]), subtitle_text, fill="#627066", font=subtitle_font)
    draw.text(((1200 - (date_box[2] - date_box[0])) / 2, 436 - date_box[1]), date_text, fill="#627066", font=date_font)
    card.save(OUT / "social-card.png", format="PNG", optimize=True)

    css = "body{font-family:serif;line-height:1.5;margin:5%;} h1{font-size:2em;} h2{font-family:sans-serif;font-size:1em;margin-top:2em;} p{margin:0 0 1em;}"
    nav_items, manifest_items, spine_items = [], [], []
    files: dict[str, str] = {"style.css": css}
    for i, (path, label, sections) in enumerate(batches, 1):
        fname = f"chapter{i:02}.xhtml"
        body = f'<h1>Plato, <em>Phaedo</em></h1><p class="subtitle">{html.escape(label)}</p>'
        body += "\n".join(f'<section id="s-{ref}"><h2>{ref}</h2>{content}</section>' for ref, content in sections)
        files[fname] = xhtml(f"Phaedo — {label}", body)
        manifest_items.append(f'<item id="c{i}" href="{fname}" media-type="application/xhtml+xml"/>')
        spine_items.append(f'<itemref idref="c{i}"/>')
        for ref, _ in sections:
            nav_items.append(f'<li><a href="{fname}#s-{ref}">{ref}</a></li>')
    files["nav.xhtml"] = xhtml("Contents", '<nav epub:type="toc" id="toc"><h1>Contents</h1><ol>' + "".join(nav_items) + '</ol></nav>')
    opf = f'''<?xml version="1.0" encoding="utf-8"?>
<package xmlns="http://www.idpf.org/2007/opf" version="3.0" unique-identifier="pub-id" xml:lang="en"><metadata xmlns:dc="http://purl.org/dc/elements/1.1/"><dc:identifier id="pub-id">{IDENT}</dc:identifier><dc:title>Phaedo: A New Translation</dc:title><dc:creator>Plato</dc:creator><dc:language>en</dc:language><dc:date>{date.today().isoformat()}</dc:date><dc:description>Modern-English translation from the Greek, with Stephanus references.</dc:description><meta property="dcterms:modified">{date.today().strftime('%Y-%m-%dT00:00:00Z')}</meta></metadata><manifest><item id="nav" href="nav.xhtml" media-type="application/xhtml+xml" properties="nav"/><item id="css" href="style.css" media-type="text/css"/>{''.join(manifest_items)}</manifest><spine>{''.join(spine_items)}</spine></package>'''
    files["content.opf"] = opf
    epub = OUT / "phaedo.epub"
    with zipfile.ZipFile(epub, "w") as zf:
        zf.writestr("mimetype", "application/epub+zip", compress_type=zipfile.ZIP_STORED)
        zf.writestr("META-INF/container.xml", '<?xml version="1.0" encoding="UTF-8"?><container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container"><rootfiles><rootfile full-path="EPUB/content.opf" media-type="application/oebps-package+xml"/></rootfiles></container>')
        for name, data in files.items():
            zf.writestr("EPUB/" + name, data, compress_type=zipfile.ZIP_DEFLATED)
    print(f"Created {OUT / 'phaedo.html'} and {epub} with {len(all_sections)} Stephanus sections.")


if __name__ == "__main__":
    main()
