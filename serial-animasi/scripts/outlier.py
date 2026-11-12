#!/usr/bin/env python3
"""Cari outlier: video animasi pendek (<=3 menit) dengan views besar dari kanal kecil."""
import re, sys, time
sys.path.insert(0, "/tmp")
from ytprobe import search, channel

THIS_MONTH_SHORT = "EgQIBBAB"   # upload bulan ini + durasi < 4 menit
THIS_WEEK_SHORT = "EgQIABBAB"   # cadangan


def dur_sec(s):
    if not s or s == "SHORT":
        return 60
    p = [int(x) for x in re.findall(r"\d+", s)]
    if len(p) == 3:
        return p[0] * 3600 + p[1] * 60 + p[2]
    if len(p) == 2:
        return p[0] * 60 + p[1]
    return p[0] if p else 0


def views_int(s):
    m = re.search(r"([\d,]+)", s or "")
    return int(m.group(1).replace(",", "")) if m else 0


def subs_num(s):
    m = re.search(r"([\d.,]+)\s*([KMB]?)", s or "")
    if not m:
        return None
    v = float(m.group(1).replace(",", ""))
    return int(v * {"K": 1e3, "M": 1e6, "B": 1e9, "": 1}[m.group(2)])


QUERIES = sys.argv[1:] or ["animation", "animasi", "3d animation", "storytime animation",
                           "horror animation", "animation meme", "claymation", "ai animation",
                           "satisfying animation", "stickman animation"]

cand = {}
for q in QUERIES:
    try:
        rows = search(q, THIS_MONTH_SHORT)
    except Exception as e:
        print(f"[gagal] {q}: {e}", file=sys.stderr)
        continue
    kept = 0
    for r in rows:
        v = views_int(r["views"])
        d = dur_sec(r["dur"])
        if v >= 100_000 and d <= 185 and r["handle"]:
            key = (r["handle"], r["title"][:40])
            if key not in cand:
                cand[key] = {**r, "v": v, "d": d, "q": q}
                kept += 1
    print(f"[{q}] {len(rows)} hasil, {kept} kandidat baru", file=sys.stderr)
    time.sleep(0.4)

print(f"\n=== {len(cand)} kandidat unik; ambil subscriber tiap kanal ===\n", file=sys.stderr)
cache = {}
out = []
for (h, _), r in cand.items():
    if h not in cache:
        try:
            cache[h] = subs_num(channel(h)["subs"])
        except Exception:
            cache[h] = None
        time.sleep(0.3)
    s = cache[h]
    ratio = (r["v"] / s) if s else None
    out.append({**r, "subs": s, "ratio": ratio})

out.sort(key=lambda x: (x["ratio"] or 0), reverse=True)
print(f"{'VIEWS':>12} | {'SUBS':>10} | {'RASIO':>7} | {'DUR':>5} | {'UMUR':<9} | {'KANAL':<26} | JUDUL")
print("-" * 140)
for r in out[:55]:
    sub = f"{r['subs']:,}" if r["subs"] else "?"
    ra = f"{r['ratio']:.1f}x" if r["ratio"] else "?"
    print(f"{r['v']:>12,} | {sub:>10} | {ra:>7} | {r['dur']:>5} | {r['age']:<9} | "
          f"{r['handle']:<26} | {r['title'][:58]}")
