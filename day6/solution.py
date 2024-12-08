with open("day6/input.txt") as f:
    map = [[y for y in x] for x in f.read().splitlines()]

# Common
def add_delta_to_position(position, delta):
    return (position[0] + delta[0], position[1] + delta[1])

def sub_delta_from_position(position, delta):
    return (position[0] - delta[0], position[1] - delta[1])

def multiply_delta_by(delta, mul):
    return (delta[0] * mul[0], delta[1] * mul[1])

def navigate_guard_path(starting_pos, starting_delta):
    unique_positions = set()
    position = starting_pos
    delta = starting_delta
    while True:
        if (position, delta) in unique_positions:
            return unique_positions, False
        
        unique_positions.add((position, delta))
        next_y, next_x = add_delta_to_position(position, delta)

        if next_y < 0 or next_y >= len(map) or next_x < 0 or next_x >= len(map[next_y]):
            return unique_positions, True
        
        if map[next_y][next_x] == "." or map[next_y][next_x] == "^":
            position = (next_y, next_x)
        else:
            delta = (delta[1], -delta[0])


start = None
for y, row in enumerate(map):
    for x, __ in enumerate(row):
        if map[y][x] == "^":
            start = (y, x)
            break

delta = (-1, 0)
# Part one
positions = navigate_guard_path(start, delta)[0]
print(len(set([x[0] for x in positions])))

# Part two
# 2008
# find "triangles"
deltas = [(0, 1), (1, 0), (0, -1), (-1, 0)]
potentials_blocks = set()

def find_block(delta, position):
    y = position[0]
    x = position[1]
    while y >= 0 and y < len(map) and x >= 0 and x < len(map[y]):
        if map[y][x] == "#":
            return (y, x)
        y = y + delta[0]
        x = x + delta[1]
    return None


def check(delta, position):
    starting_block_corrds = position
    position = sub_delta_from_position(position, delta)
 
    delta = (delta[1], -delta[0])
    second_coords = find_block(delta, position)
    if not second_coords:
        return None
    position = sub_delta_from_position(second_coords, delta)
    delta = (delta[1], -delta[0])
    third_coords = find_block(delta, position)
    if not third_coords: 
        return None
    position = sub_delta_from_position(third_coords, delta)
    delta = (delta[1], -delta[0])
    diff = multiply_delta_by(delta, starting_block_corrds)
    position = add_delta_to_position(position, diff)
    return (position, delta)

for y, row in enumerate(map):
    for x, __ in enumerate(row):
        if map[y][x] == "#":
            first_block_pos = (y, x)
            for delta in deltas:
                res = check(delta, first_block_pos)
                if res is not None:
                    potentials_blocks.add(res)
            
unique_positions = set()
position = start
delta = (-1, 0)
count = 0
print(potentials_blocks)
while True:
    unique_positions.add((position, delta))
    next_y, next_x = add_delta_to_position(position, delta)
    if ((next_y, next_x), delta) in potentials_blocks:
       print((next_y, next_x), delta)
       count +=1
    if next_y < 0 or next_y >= len(map) or next_x < 0 or next_x >= len(map[next_y]):
        break

    if map[next_y][next_x] == "." or map[next_y][next_x] == "^":
        position = (next_y, next_x)
    else:
        delta = (delta[1], -delta[0])
print(count)

"""
....#.....
.........#
..........
..#.......
.......#..
..........
.#.T^.....
......T.#.
#.........
......#...
"""

# (6, 3)
# (7, 6)
# (7, 7)
# (8, 1)
# (8, 3)
# (9, 7)
