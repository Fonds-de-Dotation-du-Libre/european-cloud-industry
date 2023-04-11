#!/usr/bin/env python3

import glob, json, os, sys

# moved to virtual environment in Python3 and installing jsonschema
#sys.path.append("/srv/slapgrid/slappart60/srv/runner/software/36024dd5826c8883cf99681c7e079a54/eggs/jsonschema-3.0.2-py2.7.egg")
#sys.path.append("/srv/slapgrid/slappart60/srv/runner/software/36024dd5826c8883cf99681c7e079a54/eggs/attrs-18.2.0-py2.7.egg")
#sys.path.append('/srv/slapgrid/slappart60/srv/runner/software/36024dd5826c8883cf99681c7e079a54/eggs/six-1.12.0-py2.7.egg')
#sys.path.append("/srv/slapgrid/slappart60/srv/runner/software/36024dd5826c8883cf99681c7e079a54/develop-eggs/pyrsistent-0.16.1-py2.7-linux-x86_64.egg")


from jsonschema import validate
from jsonschema.exceptions import ValidationError

SCHEMA = json.load(open("contribute/JSON-schema.json"))

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
        invalid_json_list.append({"file":fn, "error": e.message, "path": e.absolute_path})
        continue

    print(f"{fn} -> OK")
    num_valid += 1


print(f"{num_valid} valid JSON files\n")
print("\nfollowing file are incorrect:\n")
for fn in incorrect_json_list:
   print(f"{fn}")

print("\nfollowing file are invalid:\n")
for fn in invalid_json_list:
  print(f"{fn['file']}:\n  {fn['error']} at {fn['path']}\n")

