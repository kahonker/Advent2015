import re
import time
with open("input7", "r") as f:
    data = f.read().split("\n")
    

all_vars = {}

def find_set_vars():
    i = 0
    while i < len(data):
        line = data[i].split()
        # existing_vars = "(?:"+"|".join(all_vars.keys())+")"
        # if existing_vars != "(?:)": existing_vars = "|" + existing_vars
        # else: existing_vars = ""
        # if re.match(r"^([0-9]+" + existing_vars + ") -> [a-z]+$", line) is None:
        #     i += 1
        #     continue
        if line[1] != "->":
            i += 1
            continue
        value = line[0]
        var = line[2]
        if not value.isdigit() and value not in all_vars.keys():
            i += 1
            continue
        if value.isdigit():
            all_vars[var] = int(value)
        else:
            all_vars[var] = all_vars[value]

        data.remove(" ".join(line))

def find_and():
    i = 0
    while i < len(data):
        line = data[i].split()
        # existing_vars = "("+"|".join(all_vars.keys())+")"
        # if re.match(r"^([0-9]|" + existing_vars + ") AND (" + existing_vars + ") -> [a-z]+$", line) is None:
        #     i += 1
        #     continue
        if line[1] != "AND":
            i += 1
            continue
        value1 :str = line[0]
        value2 = line [2]
        var = line[-1]
        if (not value1.isdigit() and value1 not in all_vars.keys()) or value2 not in all_vars.keys():
            i += 1
            continue
        if value1.isdigit():
            all_vars[var] = int(value1) & all_vars[value2]
        else: all_vars[var] = all_vars[value1] & all_vars[value2]
        print(" ".join(line))
        data.remove(" ".join(line))
        print(data)


def find_or():
    i = 0
    while i < len(data):
        line = data[i].split()
        # existing_vars = "("+"|".join(all_vars.keys())+")"
        # search = r"^([0-9]|" + existing_vars + ") OR (" + existing_vars + ") -> [a-z]+$"
        # if re.match(search, line) is None:
        #     i += 1
        #     continue
        if line[1] != "OR":
            i += 1
            continue
        value1: str = line[0]
        value2 = line[2]
        var = line[-1]
        if value1 not in all_vars.keys() or value2 not in all_vars.keys():
            i += 1
            continue
        if value1.isdigit():
            all_vars[var] = int(value1) | all_vars[value2]
        else: all_vars[var] = all_vars[value1] | all_vars[value2]
        data.remove(" ".join(line))

def find_lshift():
    i = 0
    while i < len(data):
        line = data[i].split()
        # existing_vars = "("+"|".join(all_vars.keys())+")"
        # search = r"^([0-9]|" + existing_vars + ") LSHIFT [0-9]+ -> [a-z]+$"
        # if re.match(search, line) is None:
        #     i += 1
        #     continue
        if line[1] != "LSHIFT":
            i += 1
            continue
        value1: str = line[0]
        value2 = line[2]
        var = line[-1]
        if value1 not in all_vars.keys():
            i += 1
            continue
        all_vars[var] = all_vars[value1] << int(value2)
        data.remove(" ".join(line))

def find_rshift():
    i = 0
    while i < len(data):
        line = data[i].split()
        # existing_vars = "("+"|".join(all_vars.keys())+")"
        # search = r"^([0-9]|" + existing_vars + ") RSHIFT [0-9]+ -> [a-z]+$"
        # if re.match(search, line) is None:
        #     i += 1
        #     continue
        if line[1] != "RSHIFT":
            i += 1
            continue
        value1: str = line[0]
        value2 = line[2]
        var = line[-1]
        if value1 not in all_vars.keys():
            i += 1
            continue
        all_vars[var] = all_vars[value1] >> int(value2)
        data.remove(" ".join(line))

def find_not():
    i = 0
    while i < len(data):
        line = data[i].split()
        # existing_vars = "("+"|".join(all_vars.keys())+")"
        # search = r"^NOT (" + existing_vars + ") -> [a-z]+$"
        # if re.match(search, line) is None:
        #     i += 1
        #     continue
        if line[0] != "NOT":
            i += 1
            continue
        value1 :str = line[1]
        var = line[-1]
        if value1 not in all_vars.keys():
            i += 1
            continue
        all_vars[var] = ~all_vars[value1] & 0xffff
        data.remove(" ".join(line))

while len(data) > 0:
    find_set_vars()
    find_and()
    find_or()
    find_lshift()
    find_rshift()
    find_not()

print(all_vars["a"])