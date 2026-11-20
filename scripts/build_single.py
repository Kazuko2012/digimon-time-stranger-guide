#!/usr/bin/env python3
"""把主页面打包成一个自包含的单文件 HTML（图标 base64 内嵌），方便离线分发。

用法：
    python3 scripts/build_single.py
产出：
    dist/digimon-time-stranger-guide-single.html
"""
import base64
import glob
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "index.html")
OUT_DIR = os.path.join(ROOT, "dist")
OUT = os.path.join(OUT_DIR, "digimon-time-stranger-guide-single.html")

icons = {}
for f in sorted(glob.glob(os.path.join(ROOT, "assets", "icons", "*.webp"))):
    key = os.path.basename(f)[:3]
    icons[key] = "data:image/webp;base64," + base64.b64encode(open(f, "rb").read()).decode()

blob = json.dumps(icons, separators=(",", ":"))
html = open(SRC, encoding="utf-8").read()

anchor = "const PERS_CN="
if anchor not in html:
    raise SystemExit("找不到注入锚点 PERS_CN=，请检查 index.html 是否被改动")

html = html.replace(anchor, "const ICONS=" + blob + ";\n" + anchor, 1)

os.makedirs(OUT_DIR, exist_ok=True)
open(OUT, "w", encoding="utf-8").write(html)
print("output:", OUT)
print("size: %.2f MB" % (os.path.getsize(OUT) / 1048576), "icons:", len(icons))
