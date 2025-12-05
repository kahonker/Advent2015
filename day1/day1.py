import re

with open("input1", "r") as f:
    data = f.read()

floor = 0

def change_floors(up_down):
    global floor
    if up_down == ")":
        floor -= 1
    if up_down == "(":
        floor += 1

for i in range(0, len(data)):
    change_floors(data[i:i+1])
    if floor < 0:
        print(i + 1, floor)
        break

