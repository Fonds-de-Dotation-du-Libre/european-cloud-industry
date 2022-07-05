#!/usr/bin/env python3

import glob, json, os, sys
from jsonschema import validate
from jsonschema.exceptions import ValidationError

SCHEMA = json.load(open("data/JSON-schema.json"))

num_valid = 0

if len(sys.argv) > 1:
  filenames = sys.argv[1:]
else:
  filenames = sorted(glob.glob("*.json"))
incorrect_json_list = []
invalid_json_list = []

for fn in filenames:
    try:
        data = json.load(open(fn))
    except:
        incorrect_json_list.append(fn)
        continue

    try:
        validate(instance=data, schema=SCHEMA[0])
    except ValidationError as e:
        invalid_json_list.append({"file":fn, "error": e.message})
        continue

    print(f"{fn} -> OK")
    num_valid += 1


print(f"{num_valid} valid JSON files\n")
print("\nfollowing file are incorrect:\n")
for fn in incorrect_json_list:
   print(f"{fn}")

print("\nfollowing file are invalide:\n")
for fn in invalid_json_list:
  print(f"{fn['file']}: {fn['error']}")

