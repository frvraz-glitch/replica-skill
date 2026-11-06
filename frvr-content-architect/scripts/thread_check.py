#!/usr/bin/env python3
"""Check a FRVR Thread Map (CSV) for orphans, broken threads and incomplete arcs.

Usage: python3 thread_check.py thread-map.csv [--recent N]

Standard library only. Exit code 1 if any ERROR is found, else 0.
Rows with status "idea" are listed in the Idea Bank and skipped by sequence checks.
"""
import csv
import sys
from collections import Counter, defaultdict

ACTS = ["design", "distortion", "deliverance", "discipleship"]
FACES = ["SPIRIT", "SOUL", "SOMA", "SOCIAL"]
DESCENT = {"fruit", "pattern", "pain", "lie", "root", "longing"}
ASCENT = {"truth", "frame", "framework", "formation", "fruit"}


def layers(row):
    return {p.strip().lower() for p in (row.get("layer") or "").replace(",", "+").split("+") if p.strip()}


def as_int(v):
    try:
        return int(str(v).strip())
    except (TypeError, ValueError):
        return None


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        return 2
    path = argv[1]
    recent = 24
    if "--recent" in argv:
        recent = as_int(argv[argv.index("--recent") + 1]) or 24

    with open(path, newline="", encoding="utf-8-sig") as f:
        rows = [{k.strip(): (v or "").strip() for k, v in r.items() if k} for r in csv.DictReader(f)]

    errors, warns = [], []
    E = lambda m: errors.append(m)
    W = lambda m: warns.append(m)

    ideas = [r for r in rows if r.get("status", "").lower() == "idea"]
    posts = [r for r in rows if r.get("status", "").lower() != "idea"]
    ids = {r["id"] for r in rows if r.get("id")}

    seen = Counter(r.get("id") for r in rows)
    for i, n in seen.items():
        if not i:
            E("a row has no id")
        elif n > 1:
            E(f"{i}: id used {n} times")

    by_series = defaultdict(list)
    for r in posts:
        rid = r.get("id") or "?"
        act = r.get("act", "").lower()
        face = r.get("face", "").upper()
        if not r.get("series"):
            E(f"{rid}: orphan, no series (put it in a series or mark status=idea)")
        else:
            by_series[r["series"]].append(r)
        if act not in ACTS:
            E(f"{rid}: act '{r.get('act')}' is not one of {ACTS}")
        if face not in FACES:
            E(f"{rid}: face '{r.get('face')}' is not one of {FACES}")
        for k in ("prev", "next"):
            if r.get(k) and r[k] not in ids:
                E(f"{rid}: {k} points to missing id '{r[k]}'")
        if not r.get("verse"):
            W(f"{rid}: no verse reference")
        if act == "distortion" and not (r.get("surface") or r.get("lie") or r.get("root")):
            W(f"{rid}: distortion post with no surface sentence, lie or root written down")
        if act == "deliverance" and not r.get("truth"):
            W(f"{rid}: deliverance post with no truth line")
        if act == "discipleship" and ("formation" in layers(r) or "fruit" in layers(r)):
            p = r.get("protocol", "")
            if not p:
                E(f"{rid}: discipleship post with no protocol (SMART: floor, if-then, measure, duration)")
            else:
                low = p.lower()
                missing = [w for w, keys in (("floor", ["floor"]), ("if-then", ["if "]),
                                             ("measure", ["log", "track", "measure", "y/n"]),
                                             ("duration", ["day", "week"])) if not any(x in low for x in keys)]
                if missing:
                    W(f"{rid}: protocol may be missing: {', '.join(missing)}")
        if act in ("design", "discipleship") and not r.get("evidence"):
            W(f"{rid}: {act} post with no evidence claim listed (send claims to frvr-evidence-library)")

    # series completeness and threading
    for s, rs in by_series.items():
        rs.sort(key=lambda r: (as_int(r.get("part")) or 0, r.get("date", "")))
        acts = {r.get("act", "").lower() for r in rs}
        lays = set().union(*(layers(r) for r in rs))
        for need in ("distortion", "deliverance", "discipleship"):
            if need not in acts:
                E(f"series '{s}': no {need} post, so Root to Fruit is incomplete")
        if "design" not in acts and len(rs) >= 4:
            W(f"series '{s}': no design post (how it's meant to work)")
        if not ({"lie", "root"} & lays):
            W(f"series '{s}': the Descent never names a lie or root")
        offers = {r.get("offer") for r in rs if r.get("offer")}
        if not offers:
            W(f"series '{s}': no offer at the end")
        declared = {as_int(r.get("of")) for r in rs if as_int(r.get("of"))}
        if len(declared) > 1:
            E(f"series '{s}': inconsistent 'of' values {sorted(declared)}")
        elif declared and len(rs) != declared.pop():
            W(f"series '{s}': {len(rs)} posts mapped but 'of' says otherwise")
        if len(rs) > 1:
            for i, r in enumerate(rs):
                if i > 0 and not r.get("prev"):
                    E(f"{r['id']}: part {r.get('part')} of '{s}' has no prev link")
                if i < len(rs) - 1 and not r.get("next"):
                    E(f"{r['id']}: part {r.get('part')} of '{s}' has no next link")
            # turn position: deliverance shouldn't come before every distortion
            order = [r.get("act", "").lower() for r in rs]
            if "deliverance" in order and "distortion" in order:
                if order.index("deliverance") < max(i for i, a in enumerate(order) if a == "distortion"):
                    W(f"series '{s}': a distortion post comes after the turn; check the arc")

    # sequence checks per account
    by_acct = defaultdict(list)
    for r in posts:
        by_acct[r.get("account") or "?"].append(r)
    for acct, rs in by_acct.items():
        rs.sort(key=lambda r: (r.get("date", ""), r.get("id", "")))
        run = 0
        for r in rs:
            a = r.get("act", "").lower()
            run = run + 1 if a == "distortion" else 0
            if run == 3:
                W(f"{acct}: three distortion posts in a row ending {r['id']}; give the turn sooner")
        tail = rs[-recent:]
        fc = Counter(r.get("face", "").upper() for r in tail)
        ac = Counter(r.get("act", "").lower() for r in tail)
        if len(tail) >= 12:
            for face in FACES:
                if fc[face] == 0:
                    W(f"{acct}: no {face} post in the last {len(tail)}")
        # grid rows
        grid = defaultdict(list)
        for r in rs:
            if r.get("grid_row"):
                grid[r["grid_row"]].append(r)
        for g, cells in sorted(grid.items(), key=lambda kv: as_int(kv[0]) or 0):
            pos = [c.get("grid_pos", "").upper() for c in cells]
            if len(cells) != 3:
                W(f"{acct}: grid row {g} has {len(cells)} posts (rows stay aligned only in threes)")
            dup = [p for p, n in Counter(pos).items() if n > 1 and p]
            if dup:
                E(f"{acct}: grid row {g} has two posts at position {', '.join(dup)}")
        print(f"\n{acct}: {len(rs)} posts · faces " +
              " ".join(f"{f}:{fc[f]}" for f in FACES) + " · acts " +
              " ".join(f"{a}:{ac[a]}" for a in ACTS) + f" (last {len(tail)})")

    print(f"\nSeries: {len(by_series)} · Idea Bank: {len(ideas)}")
    for s, rs in by_series.items():
        print(f"  {s}: {len(rs)} posts · " + " → ".join(r.get("act", "?")[:5] for r in rs))

    for label, items in (("ERROR", errors), ("WARN", warns)):
        if items:
            print(f"\n{label}S ({len(items)})")
            for m in items:
                print(f"  {label}: {m}")
    if not errors and not warns:
        print("\nAll threads connect.")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
