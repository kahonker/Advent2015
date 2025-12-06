with open("input10", "r") as f:
    data = f.read()

seq = data

def find_next(item):
    next = ""
    count = 1
    prev_char = ""
    for char in item + " ":
        if char == prev_char:
            count += 1
        if char != prev_char and prev_char != "":
            next += str(count) + prev_char
            count = 1
        prev_char = char
    return next

for i in range(0, 50):
    seq = find_next(seq)

print(len(seq))