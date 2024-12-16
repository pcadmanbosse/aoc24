with open("day15/input.txt") as f:
    raw = f.read()
    raw_map = raw.split("\n\n")[0]
    commands = raw.split("\n\n")[1].replace("\n", "")
    map = [[x for x in y] for y in raw_map.split("\n")]


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


def move_pos(pos, direction, el) -> tuple:
    if direction == "^":
        delta = (-1, 0)
    elif direction == ">":
        delta = (0, 1)
    elif direction == "v":
        delta = (1, 0)
    elif direction == "<":
        delta = (0, -1)
    else:
        raise ValueError("Wrong direction")

    candidate_coord = add(pos, delta)
    y, x = to_y_x(candidate_coord)
    if map[y][x] == "#":
        return None
    if map[y][x] == ".":
        map[y][x] = el
        return candidate_coord
    if move_pos(candidate_coord, direction, map[y][x]) != None:
        map[y][x] = el
        return candidate_coord


# Part 1
for y, row in enumerate(map):
    for x, _ in enumerate(row):
        if map[y][x] == "@":
            at_pos = (y, x)


next_coord = at_pos
for c in commands:
    cand = move_pos(next_coord, c, "@")
    if cand is not None:
        y, x = to_y_x(next_coord)
        map[y][x] = "."
        next_coord = cand
score = 0
for y, row in enumerate(map):
    for x, _ in enumerate(row):
        if map[y][x] == "O":
            score = score + (y) * 100 + x

print(score)

# Part 2
with open("day15/input.txt") as f:
    raw = f.read()
    raw_map = raw.split("\n\n")[0].split("\n")
    commands = raw.split("\n\n")[1].replace("\n", "")

map = []
for row in raw_map:
    new_map_row = []
    for entry in row:
        if entry == ".":
            new_map_row.extend([".", "."])
        elif entry == "@":
            new_map_row.extend(["@", "."])
        elif entry == "#":
            new_map_row.extend(["#", "#"])
        elif entry == "O":
            new_map_row.extend(["[", "]"])
    map.append(new_map_row)

for y, row in enumerate(map):
    for x, _ in enumerate(row):
        if map[y][x] == "@":
            at_pos = (y, x)


def move_pos(og, direction):
    if direction == "^":
        delta = (-1, 0)
    elif direction == ">":
        delta = (0, 1)
    elif direction == "v":
        delta = (1, 0)
    elif direction == "<":
        delta = (0, -1)
    else:
        raise ValueError("Wrong direction")

    queue = [og]
    shift_coords = []
    while len(queue) > 0:
        check_coord = queue.pop(0)
        
        y, x = to_y_x(check_coord)
        el = map[y][x]
        next_position_to_visit = add(check_coord, delta)
        if el == ".":
            continue
        if check_coord not in shift_coords:
            shift_coords.append(check_coord)
        if el == "#":
            return None
        else:
            if delta == (0, -1) or delta == (0, 1) or el == "@":
                queue.append(next_position_to_visit)
            else:
                if map[y][x] == "[":
                    offset_pos = add(next_position_to_visit, (0, 1))
                    history_add = add(check_coord, (0,1))
                elif map[y][x] == "]":
                    offset_pos = add(next_position_to_visit, (0, -1))
                    history_add = add(check_coord, (0,-1))
                if history_add not in shift_coords:
                    shift_coords.append(history_add)
                queue.append(next_position_to_visit)
                queue.append(offset_pos)
    while len(shift_coords) > 0:
        next_el = shift_coords.pop()
        y, x = to_y_x(next_el)
        deltaed = add(next_el, delta)
        dy, dx = to_y_x(deltaed)
        map[dy][dx] = map[y][x]
        map[y][x] = "."
    return add(og, delta)


next_coord = at_pos
for y, row in enumerate(map):
    r = []
    for x, _ in enumerate(row):
        r.append(map[y][x])
    print("".join(r))
for y, row in enumerate(map):
    r = []
    for x, _ in enumerate(row):
        r.append(map[y][x])
for c in commands:
    cand = move_pos(next_coord, c)
    count = 0
    if cand != None:
        next_coord = cand
        
score = 0
for y, row in enumerate(map):
    for x, _ in enumerate(row):
        if map[y][x] == "[":
            score = score + (y) * 100 + x

print(score)
