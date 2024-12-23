from queue import PriorityQueue

with open("day20/input.txt") as f:
    map = [[x for x in y] for y in f.read().splitlines()]


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


rotations = [(0, -1), (-1, 0), (0, 1), (1, 0)]

# Part 1
def manhattan(pos, pos2):
    return abs(pos2[0] - pos[0]) + abs(pos2[1]-pos[1])

def djikstras(cheats_allowed, pre_visited, best_val, start_char, end_char):
    for y, row in enumerate(map):
        for x, _ in enumerate(row):
            if map[y][x] == start_char:
                start_pos = (y, x)
    for y, row in enumerate(map):
        for x, _ in enumerate(row):
            if map[y][x] == start_char:
                end_pos = (y, x)
    manhattan_map = []
    for y, row in enumerate(map):
        n_r = []
        for x, _ in enumerate(row):
            n_r.append(manhattan((end_pos), (y,x)))
        manhattan_map.append(n_r)
        
    if best_val is None:
        best_val = len(map) ** len(map)

    visited = {}
    queue = []
    queue.append((0, start_pos, '', (-1, -1)))
    cheat_map = {}
    while len(queue)> 0:
        (cost, coordinates, prev_cheats, prev) = queue.pop()
        number_of_cheats = len(prev_cheats.split(","))
        cheats_left = cheats_allowed - number_of_cheats
        y, x = to_y_x(coordinates)
        if not is_in_map_bounds(coordinates) or map[y][x] == "#" and map[prev[0]][prev[1]] == "#":
            continue
        elif (
            (
                (coordinates, prev_cheats) not in visited
                or visited[(coordinates, prev_cheats)] > cost
            )
            and not (cost > best_val)
            and not (
                (coordinates, '') in visited
                and visited[(coordinates, '')] < cost
            )
        ):
            visited[(coordinates, prev_cheats)] = cost
            
            if cheats_allowed == 0 and map[y][x] == end_char:
                cheat_map[prev_cheats] = min(cheat_map.get(prev_cheats, len(map)**len(map)), cost)
            elif manhattan_map[y][x] <= cheats_left:
                cheat_map[prev_cheats] = min(cheat_map.get(prev_cheats, len(map)**len(map)), cost + manhattan_map[y][x])
            elif len(prev_cheats.split(",")) == 20 and (((coordinates, '') in pre_visited) or map[y][x] == end_char): 
                pre_cost = pre_visited[(coordinates, '')]
                if pre_cost + cost <= best_val:
                    cheat_map[prev_cheats] = min(
                        cheat_map.get(prev_cheats, len(map) ** len(map)), cost + pre_cost
                    )
            else:
                if (cheats_allowed == 0 or number_of_cheats == cheats_allowed) and map[y][x] == "#":
                    continue
                if map[y][x] == "#":
                    if prev_cheats == '':
                        prev_cheats = f"{prev[0]}:{prev[1]}"
                    prev_cheats += f",{y}:{x}"
                for rotation in rotations:
                    added = add(coordinates, rotation)
                    if added != prev:
                        queue.append(
                            (
                                cost + 1,
                                add(coordinates, rotation),
                                prev_cheats,
                                coordinates,
                            )
                        )

    return len(cheat_map), visited, cheat_map.get('', 0)

tots, pre_visited, best_cost = djikstras(0, None, None, "E", "S")
print
print(best_cost)
print(djikstras(2, pre_visited, best_cost, "S", "E")[0])
print(djikstras(20, pre_visited, best_cost, "S", "E")[0])
