#!/usr/bin/env python3
"""Hand-label snippets: y = AI should speak, n = stay quiet, s = skip, q = quit. Resumes where you left off."""
import csv, json, os
DATA, OUT = "data/snippets.jsonl", "data/labels.csv"
done = {}
if os.path.exists(OUT):
    with open(OUT) as f:
        done = {r["id"]: r for r in csv.DictReader(f)}
rows = [json.loads(l) for l in open(DATA)]
new = not os.path.exists(OUT)
with open(OUT, "a", newline="") as f:
    w = csv.DictWriter(f, fieldnames=["id", "label", "why"])
    if new: w.writeheader()
    for r in rows:
        if r["id"] in done: continue
        print(f"\n--- {r['id']} ---")
        for line in r["transcript"]: print("  " + line)
        a = input(f"{r['question']} [y/n/s/q] ").strip().lower()
        if a == "q": break
        if a not in ("y", "n"): continue
        why = input("  one-line reason (critique, Hamel style): ").strip()
        w.writerow({"id": r["id"], "label": "pass" if a == "y" else "fail", "why": why}); f.flush()
print(f"\nLabelled so far: saved in {OUT}")
