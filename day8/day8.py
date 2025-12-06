import re

with open("input8", "r") as f:
    data = f.read().split("\n")

literal_sum = 0
character_sum = 0

for line in data:
    literal_sum += len(line)
    new_line = re.escape(line)
    new_line = new_line.replace("\"", "\\\"")
    print(new_line)
    character_sum += len(new_line) + 2


print(character_sum - literal_sum)