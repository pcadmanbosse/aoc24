with open("day12/input.txt") as f:
    map = [[y for y in x] for x in f.read().splitlines()]

# Part 1
regions = []
visited = set()


def is_in_map_bounds(position):
    return (
        position[0] >= 0
        and position[0] < len(map)
        and position[1] >= 0
        and position[1] < len(map[0])
    )


def to_y_x(position):
    return position[0], position[1]


def dfs(starting_position):
    if starting_position in visited:
        return 0
    y, x = to_y_x(starting_position)
    starting_pattern = map[y][x]
    perimeter = 0
    area = 0
    queue = [starting_position]
    while len(queue) > 0:
        next_element = queue.pop()
        next_y, next_x = to_y_x(next_element)
        if not is_in_map_bounds(next_element):
            perimeter += 1
        elif map[next_y][next_x] != starting_pattern:
            perimeter +=1
        elif not next_element in visited:
            area += 1
            queue.append((next_y -1, next_x))
            queue.append((next_y +1, next_x))
            queue.append((next_y, next_x +1))
            queue.append((next_y, next_x -1))
            visited.add(next_element)

    return perimeter * area

total = 0
for y, row in enumerate(map):
    for x, _ in enumerate(row):
        total += dfs((y,x))
print(total)

# Part 2
def add(position, delta):
    return (position[0] + delta[0], position[1] + delta[1])

def handle_same_side(position, side_delta, candidate_search_direction, side_exclusion):
    original = map[position[0]][position[1]]
    pos = add(position, candidate_search_direction)
    if not is_in_map_bounds(pos) or map[pos[0]][pos[1]] != original:
        return
    offset = add(pos, side_delta)
    if not is_in_map_bounds(offset) or map[offset[0]][offset[1]] != original:
        side_exclusion.add((pos, side_delta))
        handle_same_side(pos, side_delta, candidate_search_direction, side_exclusion)

def count_sides(position, side_exclusion):
    y, x = to_y_x(position)
    initial = map[y][x]
    number_of_new_sides = 0
    angles = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    for index, delta in enumerate(angles):
        offset_coords = add(delta, position)
        if (not is_in_map_bounds(offset_coords) or map[offset_coords[0]][offset_coords[1]] != initial) and  \
        (position, delta) not in side_exclusion:
            side_exclusion.add((position, delta))
            number_of_new_sides += 1
            side_candidates = [angles[index - 1 if index > 0 else len(angles) -1],
                               angles[(index+1)%len(angles)]]
            for cand in side_candidates:
                handle_same_side(position, delta, cand, side_exclusion)
        
    return number_of_new_sides

visited = set()
def dfs_2(starting_position):
    if starting_position in visited:
        return 0
    y, x = to_y_x(starting_position)
    starting_pattern = map[y][x]
    area = 0
    edges = 0
    queue = [starting_position]
    exclusions = set()
    while len(queue) > 0:
        next_element = queue.pop()
        next_y, next_x = to_y_x(next_element)
        if not is_in_map_bounds(next_element) or map[next_y][next_x] != starting_pattern:
            continue
        if not next_element in visited:
            area += 1
            queue.append((next_y -1, next_x))
            queue.append((next_y +1, next_x))
            queue.append((next_y, next_x +1))
            queue.append((next_y, next_x -1))
            visited.add(next_element)
            edges += count_sides(next_element, exclusions)
    return area*edges

total = 0
for y, row in enumerate(map):
    for x, _ in enumerate(row):
        total += dfs_2((y,x))
print(total)
