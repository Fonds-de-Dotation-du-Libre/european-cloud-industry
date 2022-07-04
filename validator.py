
here’s a script to run the checks:

```
#!/usr/bin/env python3

import glob, json, os

from jsonschema import validate
from jsonschema.exceptions import ValidationError

SCHEMA = json.load(open("data/JSON-schema.json"))

num_valid = 0

filenames = sorted(glob.glob("data/*.json"))
for fn in filenames:
    if fn == "data/JSON-schema.json":
        continue

    try:
        data = json.load(open(fn))
    except:
        print(f"{fn} -> syntactically incorrect JSON")
        continue

    try:
        validate(instance=data, schema=SCHEMA[0])
    except ValidationError as e:
        print(f"{fn} -> invalid JSON")
        print("   " + e.message)
        continue

    print(f"{fn} -> OK")
    num_valid += 1


print(f"{num_valid} valid JSON files")
```
