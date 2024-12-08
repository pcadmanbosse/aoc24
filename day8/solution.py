with open("day8/input.txt") as f:
    map = [[y for y in x] for x in f.read().splitlines()]

# Part 1 
position_map = {}
antinodes = set()

def is_in_map_bounds(y, x):
    return y >= 0 and x >= 0 and y < len(map) and x < len(map[0])

for y, row in enumerate(map):
    for x, _ in enumerate(row):
        element_at_position = map[y][x]
        if element_at_position != ".":
            position_map[element_at_position] = position_map.get(element_at_position, set())
            for other_same_element_position in position_map[element_at_position]:
                diff_vector = (y - other_same_element_position[0], x - other_same_element_position[1])

                if is_in_map_bounds(y + diff_vector[0], x + diff_vector[1]):
                    antinodes.add((y + diff_vector[0], x + diff_vector[1]))
                if is_in_map_bounds(other_same_element_position[0] - diff_vector[0], other_same_element_position[1] - diff_vector[1]):
                    antinodes.add((other_same_element_position[0] - diff_vector[0], other_same_element_position[1] - diff_vector[1]))
            position_map[element_at_position].add((y, x))
            
print(len(antinodes))


# Part 2
position_map = {}
antinodes = set()

def is_in_map_bounds(v):
    y = v[0]
    x = v[1]
    return y >= 0 and x >= 0 and y < len(map) and x < len(map[0])

def add(v1, v2):
    return (v1[0] + v2[0], v1[1] + v2[1])

def sub(v1, v2):
    return (v1[0] - v2[0], v1[1] - v2[1])

for y, row in enumerate(map):
    for x, _ in enumerate(row):
        element_at_position = map[y][x]
        if element_at_position != ".":
            position_map[element_at_position] = position_map.get(element_at_position, set())
            for other_same_element_position in position_map[element_at_position]:
                antinodes.add(other_same_element_position)
                antinodes.add((y,x))
                diff_vector = sub((y,x), other_same_element_position)
                next_cand = add((y,x), diff_vector)
                while is_in_map_bounds(next_cand):
                    antinodes.add(next_cand)
                    next_cand = add(next_cand, diff_vector)
                next_cand = sub(other_same_element_position, diff_vector)
                while is_in_map_bounds(next_cand):
                    antinodes.add(next_cand)
                    next_cand = sub(next_cand, diff_vector)
            position_map[element_at_position].add((y, x))
            
print(len(antinodes))
