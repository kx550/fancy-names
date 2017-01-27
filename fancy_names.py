import json
import random as r
with open('names.json') as name_data:
    data = json.load(name_data)

def rand():
    return "%s %s" % (data[r.randrange(0, len(data))]["name"], data[r.randrange(0, len(data))]["surname"])

def all():
    for e in data:
        print "%s %s" % (e["name"], e["surname"])
    return

def num():
    return "%s" % (len(data))
