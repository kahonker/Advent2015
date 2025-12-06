from itertools import permutations

with open("input9", "r") as f:
    data = f.read().split("\n")

distances = []

locations = []

smallest_dist = 1000000000000000000000000000000000
largest_dist = 0

for item in data:
    distance = item.split()
    location = [distance[0], distance[2], int(distance[4])]
    distances.append(location)
    if location[0] not in locations:
        locations.append(location[0])
    if location[1] not in locations:
        locations.append(location[1])


def find_distance(location_list):
    sum_of_distances = 0
    for i in range(0, len(location_list) - 1):
        location1 = location_list[i]
        location2 = location_list[i+1]
        for item in distances:
            if location1 in item and location2 in item:
                sum_of_distances += item[2]
    return sum_of_distances

for list in permutations(locations):
    distance = find_distance(list)
    smallest_dist = distance if distance < smallest_dist else smallest_dist
    largest_dist = distance if distance > largest_dist else largest_dist

print(smallest_dist)
print(largest_dist)