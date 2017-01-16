#!/usr/bin/env python

import json
import yaml
import pprint

pp = pprint.PrettyPrinter(indent=4)


with open("file.yml") as f:
    y = yaml.load(f)
    pp.pprint(y)

with open("file.json") as f:
    j = json.load(f)
    pp.pprint(j)

print '\n'
