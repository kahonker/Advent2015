with open("input2", "r") as f:
    data = f.read().split("\n")

total_area = 0

def get_area(dimensions):
    split_dimensions = dimensions.split("x")
    measure1 = int(split_dimensions[0])
    measure2 = int(split_dimensions[1])
    measure3 = int(split_dimensions[2])
    side1 = measure1 * measure2
    side2 = measure2 * measure3
    side3 = measure3 * measure1
    return 2*side1 + 2*side3 + 2*side2 + min(side1, min(side2, side3))

def get_length(dimensions):
    split_dimensions = dimensions.split("x")
    measure1 = int(split_dimensions[0])
    measure2 = int(split_dimensions[1])
    measure3 = int(split_dimensions[2])
    side1 = 2*measure1 + 2*measure2
    side2 = 2*measure2 + 2*measure3
    side3 = 2*measure3 + 2*measure1
    return measure1 * measure2 * measure3 + min(side1, min(side2, side3))

for string in data:
    total_area += get_length(string)

print(total_area)