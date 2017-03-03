import json
import random as r
with open('names.json') as name_data:
    data = json.load(name_data)

def randomize():
    """Randomize some stuff!"""
    return "%s %s" % (data[r.randrange(0, len(data))]["name"], data[r.randrange(0, len(data))]["surname"])

def rand():
    index = r.randrange(0, len(data))
    return "%s %s" % (data[index]["name"], data[index]["surname"])

def name(index):
    return "%s %s" % (data[index]["name"], data[index]["surname"])

def all():
    for e in data:
        print "%s %s" % (e["name"], e["surname"])
    return

def add():
    print "first name:"
    name = raw_input()
    print "last name:"
    surname = raw_input()
    new_entry = {"name": name, "surname": surname}
    data.append(new_entry)
    with open('names.json', 'w') as n:
        json.dump(data, n, sort_keys=True, indent=4, separators=(',', ': '))
    return "%s %s" % (name, surname)

def num():
    return "%s" % (len(data))
