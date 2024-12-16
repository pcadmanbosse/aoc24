from queue import PriorityQueue

with open("day16/input.txt") as f:
    map = [[x for x in y] for y in f.readlines()]

for y, row in enumerate(map):
    for x, _ in enumerate(row):
        if map[y][x] == "S":
            start_pos = (y,x)

def is_in_map_bounds(position):
    return (
        position[0] >= 0
        and position[0] < len(map)
        and position[1] >= 0
        and position[1] < len(map[0])
    )


def add(position, delta):
    return (position[0] + delta[0], position[1] + delta[1])


def to_y_x(position):
    return position[0], position[1]

# Part 1 
visited = {}
queue = PriorityQueue()
queue.put((0, (start_pos, 0)))
rotations = [(0, -1), (-1, 0), (0, 1), (1, 0)]
while queue:
    next_el = queue.get()
    cost = next_el[0]
    coordinates = next_el[1][0]
    angle_index = next_el[1][1]

    y, x = to_y_x(coordinates)
    if not is_in_map_bounds(coordinates) or map[y][x] == "#":
        continue
    if (coordinates, angle_index) not in visited or visited[(coordinates, angle_index)] > cost:
        visited[(coordinates, angle_index)] = cost
    else: 
        continue
   
    if map[y][x] == "E":
        print(cost)
        break

    queue.put((cost + 1, (add(rotations[angle_index], coordinates),angle_index)))
    queue.put((cost+1000, (coordinates, (angle_index+1)%len(rotations))))
    next_an = len(rotations) - 1 if angle_index -1 == -1 else angle_index -1
    queue.put((cost+1000, (coordinates, next_an)))


# Part 2
visited = {}
cbs = set()
best_cost = -1
queue = PriorityQueue()
queue.put((0, (start_pos, 0, [start_pos])))
rotations = [(0, -1), (-1, 0), (0, 1), (1, 0)]
while queue:
    next_el = queue.get()
    cost = next_el[0]
    coordinates = next_el[1][0]
    angle_index = next_el[1][1]
    path = next_el[1][2]
    if cost > best_cost and best_cost != -1:
        break
    y, x = to_y_x(coordinates)
    if not is_in_map_bounds(coordinates) or map[y][x] == "#":
        continue
    if (coordinates, angle_index) not in visited or visited[(coordinates, angle_index)] >= cost:
        visited[(coordinates, angle_index)] = cost
    else: 
        continue
    if map[y][x] == "E":
        if best_cost == cost:
            for p in path:
                cbs.add(p)
        elif best_cost == -1 or best_cost > cost:
            best_cost = cost
            cbs = set(path)
        continue
    np = path+[coordinates] if coordinates not in path else path
    queue.put((cost + 1, (add(rotations[angle_index], coordinates),angle_index, np)))
    queue.put((cost+1000, (coordinates, (angle_index+1)%len(rotations), np)))
    next_an = len(rotations) - 1 if angle_index -1 == -1 else angle_index -1
    queue.put((cost+1000, (coordinates, next_an, np)))

print(len(cbs))