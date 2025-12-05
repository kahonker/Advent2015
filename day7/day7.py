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

        
find_set_vars()
