#!/usr/bin/env python

import json
import yaml

my_list = range(5)
my_list.append('router1')

my_list.append({})
my_list[-1]['item1'] = "this is item 1"
my_list[-1]['item2'] = "this is item 2"

print "The list is: "
print my_list

with open("file.yml", "w") as f:
    yaml.dump(my_list,f)


with open("file.json", "w") as f:
    json.dump(my_list, f)
