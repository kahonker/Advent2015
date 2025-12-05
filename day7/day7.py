import re

with open("input7", "r") as f:
    data = f.read().split("\n")
    

all_vars = {}

def find_set_vars():
    i = 0
    while i < len(data):
        line = data[i]
        print(line)
        if re.match(r"^[0-9]+ -> [a-z]+$", line) is None:
            i += 1
            continue
            
        value = int(re.findall(r"^[0-9]+", line)[0])
        var = re.findall("[a-z]+$", line)[0]
        all_vars[var] = value
        data.remove(line)

def find_and():
    i = 0
    while i < len(data):
        line = data[i]
        existing_vars = "|".join(all_vars.keys())
        if re.match(r"^([0-9]|" + existing_vars + ")+ AND (" + existing_vars + ")+ -> [a-z]+$", line) is None:
            i += 1
            continue

        value1 :str = re.findall(r"^.+ AND", line)[0][0:-4]
        value2 = re.findall(r"AND [a-z]+", line)[0][4:]
        var = re.findall("[a-z]+$", line)[0]
        if value1.isdigit():
            all_vars[var] = int(value1) & all_vars[value2]
        else: all_vars[var] = all_vars[value1] & all_vars[value2]
        data.remove(line)


def find_or():
    i = 0
    while i < len(data):
        line = data[i]
        existing_vars = "|".join(all_vars.keys())
        if re.match(r"^([0-9]|" + existing_vars + ")+ OR (" + existing_vars + ")+ -> [a-z]+$", line) is None:
            i += 1
            continue

        value1 :str = re.findall(r"^.+ OR", line)[0][0:-4]
        value2 = re.findall(r"OR [a-z]+", line)[0][4:]
        var = re.findall("[a-z]+$", line)[0]
        print(value1)
        if value1.isdigit():
            all_vars[var] = int(value1) | all_vars[value2]
        else: all_vars[var] = all_vars[value1] | all_vars[value2]
        data.remove(line)

find_set_vars()
find_and()
find_or()

print(all_vars)
