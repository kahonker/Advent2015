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
            
        value = re.findall(r"^[0-9]+", line)[0]
        var = re.findall("[a-z]+$", line)[0]
        all_vars[var] = value
        data.remove(line)

def set_values():
    i = 0
    while i < len(data):
        line = data[i]
        if re.match(r"^(" + "|".join(all_vars) + r"|[a-z]) .+ [] -> [a-z]+$", line) is None:
            i += 1
            continue

        value = re.findall(r"^[0-9]+", line)[0]
        var = re.findall("[a-z]+$", line)[0]
        all_vars[var] = value
        data.remove(line)

def find_and():
    i = 0
    while i < len(data):
        line = data[i]
        print(line)
        if re.match(r"^([a-z]+|[0-9]+) AND [a-z]+ -> [a-z]+$", line) is None:
            i += 1
            continue

        value1 = re.findall(r"^([a-z]+|[0-9]+)", line)[0]
        value2 = re.findall(r" AND [a-z]+", line)[0][5:]
        if value1 in all_vars.keys() and value2 in all_vars.keys():
            var = re.findall("[a-z]+$", line)[0]
            all_vars[var] = 
            data.remove(line)
        
find_set_vars()
