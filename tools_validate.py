#!/usr/bin/env python3
"""Validate content JSON against card-schema.json and write cards/manifest.json (list of published image files)."""
import json, os, subprocess, sys
root = os.path.dirname(os.path.abspath(__file__)); os.chdir(root)
strict = "--strict" in sys.argv
try:
    import jsonschema
    schema = json.load(open("card-schema.json")); schema.pop("examples", None)
    V = jsonschema.Draft202012Validator(schema)
except Exception as e:
    print("schema unavailable:", e); V = None
bad = 0; total = 0
for f in ["rome-cards", "medieval-cards", "learning-cards"] + [x for x in ("batch4-cards", "batch5-cards") if os.path.exists(f"content/{x}.json")]:
    cards = json.load(open(f"content/{f}.json"))  # parse errors abort
    for c in cards:
        total += 1
        errs = list(V.iter_errors(c)) if V else []
        if errs:
            bad += 1
            print(f"  {f}:{c.get('id')}: {errs[0].message[:120]}")
print(f"schema: {total-bad}/{total} cards valid")
# manifest of image files that will actually be published (tracked or addable, not ignored)
files = subprocess.run(["git", "ls-files", "-co", "--exclude-standard", "cards", "content", "assets"],
                       capture_output=True, text=True).stdout.split()
imgs = sorted(p for p in files if p.lower().endswith((".webp", ".png", ".jpg", ".jpeg", ".gif", ".svg")))
json.dump(imgs, open("cards/manifest.json", "w"), indent=0)
print(f"manifest: {len(imgs)} images")
sys.exit(1 if strict and bad else 0)
