#!/usr/bin/env python3
"""Ambil data publik YouTube (search + channel) tanpa login, parse ytInitialData."""
import json, re, sys, urllib.request, urllib.parse

UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36")


def get(url):
    req = urllib.request.Request(url, headers={
        "User-Agent": UA,
        "Accept-Language": "en-US,en;q=0.9,id;q=0.8",
        "Cookie": "CONSENT=YES+cb.20240101-00-p0.en+FX+000; SOCS=CAI",
    })
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read().decode("utf-8", "replace")


def initial_data(html):
    for pat in (r"var ytInitialData = (\{.*?\});</script>",
                r'window\["ytInitialData"\] = (\{.*?\});'):
        m = re.search(pat, html, re.S)
        if m:
            try:
                return json.loads(m.group(1))
            except Exception:
                pass
    return None


def walk(node, key):
    """Hasilkan semua dict yang punya `key`."""
    if isinstance(node, dict):
        if key in node:
            yield node
        for v in node.values():
            yield from walk(v, key)
    elif isinstance(node, list):
        for v in node:
            yield from walk(v, key)


def txt(o):
    if not o:
        return ""
    if isinstance(o, str):
        return o
    if isinstance(o, dict):
        if "runs" in o and isinstance(o["runs"], list):
            return "".join(r.get("text", "") for r in o["runs"] if isinstance(r, dict))
        return o.get("simpleText") or o.get("content") or ""
    return ""


def search(query, sp=""):
    url = "https://www.youtube.com/results?search_query=" + urllib.parse.quote(query)
    if sp:
        url += "&sp=" + sp
    data = initial_data(get(url))
    if not data:
        return []
    rows = []
    for vr in walk(data, "videoRenderer"):
        v = vr["videoRenderer"]
        owner = (v.get("ownerText") or {}).get("runs", [{}])[0]
        thumbs = (v.get("thumbnail") or {}).get("thumbnails") or [{}]
        rows.append({
            "id": v.get("videoId", ""),
            "title": txt(v.get("title"))[:70],
            "views": txt(v.get("viewCountText")),
            "age": txt(v.get("publishedTimeText")),
            "dur": txt(v.get("lengthText")),
            "ch": txt(owner)[:30],
            "thumb": thumbs[-1].get("url", ""),
            "handle": owner.get("navigationEndpoint", {})
                      .get("commandMetadata", {}).get("webCommandMetadata", {})
                      .get("url", ""),
        })
    # shorts lockup model
    for lk in walk(data, "shortsLockupViewModel"):
        s = lk["shortsLockupViewModel"]
        try:
            t = txt(s["overlayMetadata"]["primaryText"])
            v = txt(s["overlayMetadata"]["secondaryText"])
        except Exception:
            continue
        rows.append({"title": t[:70], "views": v, "age": "", "dur": "SHORT",
                     "ch": "", "handle": ""})
    return rows


def channel(handle):
    url = handle if handle.startswith("http") else "https://www.youtube.com/" + handle.lstrip("/")
    html = get(url)
    # Header kanal ada di metadataParts; halaman juga memuat subscriber kanal lain di rak
    # rekomendasi, jadi pola "subscriberCountText" pertama BUKAN milik kanal ini.
    subs = vids = ""
    m = re.search(r'"metadataParts":\[\{"text":\{"content":"([^"]*subscribers?)"\}', html)
    if m:
        subs = m.group(1)
    m2 = re.search(r'"metadataParts":\[\{"text":\{"content":"[^"]*subscribers?"\}\},\{"text":\{"content":"([^"]*videos?)"\}', html)
    if m2:
        vids = m2.group(1)
    desc = ""
    m3 = re.search(r'<meta name="description" content="([^"]{0,200})', html)
    if m3:
        desc = m3.group(1)
    return {"url": url, "subs": subs or "?", "videos": vids or "?", "desc": desc[:160]}


if __name__ == "__main__":
    mode = sys.argv[1]
    if mode == "search":
        q = sys.argv[2]
        sp = sys.argv[3] if len(sys.argv) > 3 else ""
        rows = search(q, sp)
        print(f"### {q!r} sp={sp}  -> {len(rows)} hasil")
        for r in rows[:25]:
            print(f"  {r['views']:>14} | {r['age']:<10} | {r['dur']:<7} | "
                  f"{r['ch']:<26} | {r['handle']:<22} | {r['title']}")
    elif mode == "channel":
        for h in sys.argv[2:]:
            info = channel(h)
            print(f"{h:<32} subs={info['subs']:<18} videos={info['videos']:<8} {info['desc'][:100]}")
