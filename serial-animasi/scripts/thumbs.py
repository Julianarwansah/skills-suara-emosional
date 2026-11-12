#!/usr/bin/env python3
"""Unduh thumbnail (hqdefault) dari video animasi pendek bulan ini untuk penilaian gaya visual."""
import os, re, sys, time, urllib.request
sys.path.insert(0, "/tmp")
from ytprobe import search

OUT = "/tmp/thumbs"
os.makedirs(OUT, exist_ok=True)
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/131 Safari/537.36"


def dur_sec(s):
    p = [int(x) for x in re.findall(r"\d+", s or "")]
    if len(p) == 3: return p[0]*3600 + p[1]*60 + p[2]
    if len(p) == 2: return p[0]*60 + p[1]
    return p[0] if p else 60


def views_int(s):
    m = re.search(r"([\d,]+)", s or "")
    return int(m.group(1).replace(",", "")) if m else 0


def safe(s):
    return re.sub(r"[^A-Za-z0-9]+", "_", s)[:46].strip("_")


queries = sys.argv[1:]
manifest = []
seen = set()
for q in queries:
    try:
        rows = search(q, "EgQIBBAB")
    except Exception as e:
        print(f"[gagal] {q}: {e}", file=sys.stderr); continue
    for r in rows:
        if not r.get("id") or r["id"] in seen:
            continue
        if views_int(r["views"]) < 100_000 or dur_sec(r["dur"]) > 185:
            continue
        seen.add(r["id"])
        name = f"{safe(r['handle'])}__{safe(r['title'])}"
        path = os.path.join(OUT, name + ".jpg")
        url = f"https://img.youtube.com/vi/{r['id']}/hqdefault.jpg"
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            data = urllib.request.urlopen(req, timeout=20).read()
            with open(path, "wb") as f:
                f.write(data)
            manifest.append((name, r["views"], r["dur"], r["handle"], r["title"]))
        except Exception as e:
            print(f"[thumb gagal] {name}: {e}", file=sys.stderr)
        time.sleep(0.2)

print(f"\n{len(manifest)} thumbnail tersimpan di {OUT}\n")
for name, v, d, h, t in manifest:
    print(f"{v:>14} | {d:<6} | {h:<24} | {t[:52]}")
    print(f"                 -> {name}.jpg")
