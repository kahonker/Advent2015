import re

with open("input6", "r") as f:
    data = f.read().split("\n")
    
lights_list = []
    
def setup():
    for i in range(0,1000):
        line = []
        for j in range(0,1000):
            line.append(0)
        lights_list.append(line.copy())
        
def turn_on(start, end):
    for i in range(start[0],end[0]+1):
        for j in range(start[1],end[1]+1):
            lights_list[i][j] += 1

def turn_off(start, end):
    for i in range(start[0],end[0]+1):
        for j in range(start[1],end[1]+1):
            lights_list[i][j] -= 1
            if lights_list[i][j] < 0:
                lights_list[i][j] = 0
            
def toggle(start, end):
    for i in range(start[0],end[0]+1):
        for j in range(start[1],end[1]+1):
            lights_list[i][j] += 2
            
def get_directions(string):
    find = re.findall(r"[0-9]+,[0-9]+", string)
    start = find[0].split(",")
    start = list(map(lambda i: int(i), start))
    end = find[1].split(",")
    end = list(map(lambda i: int(i), end))
    if re.match(r"^turn on", string):
        turn_on(start, end)
    elif re.match(r"^turn off", string):
        turn_off(start, end)
    else:
        toggle(start, end)
        
def find_on():
    sum = 0
    for i in range(0, len(lights_list)):
        for j in range(0, len(lights_list[i])):
            sum += lights_list[i][j]
    return sum
        
setup()

for line in data:
    get_directions(line)
    
print(find_on())