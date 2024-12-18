from queue import PriorityQueue


with open("day18/input.txt") as f:
    lines = f.read().splitlines()

map = []
for i in range(71):
    row = []
    for i in range(71):
        row.append(".")
    map.append(row)

for memseg in lines[:1024]:
    [x, y] = memseg.split(",")
    map[int(y)][int(x)] = "#"


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


deltas = [(0, -1), (-1, 0), (0, 1), (1, 0)]


# Part 1
# dfs
def search(start):
    visited = {}
    queue = PriorityQueue()
    queue.put((0, start))
    while queue:
        if queue.empty():
            return False
        (cost, position) = queue.get()
        if position not in visited or visited[position] > cost:
            visited[position] = cost
            if position[0] == len(map) - 1 and position[1] == len(map) - 1:
                return cost
            for delta in deltas:
                added = add(position, delta)
                y, x = to_y_x(added)
                if is_in_map_bounds(added) and map[y][x] == ".":
                    queue.put((cost + 1, added))
    return False


print(search((0, 0)))

# Part 2

b = 1024
t = len(lines) -1
while b != t -1:
    i = (b+t)//2
    map = []
    for _ in range(71):
        row = []
        for __ in range(71):
            row.append(".")
        map.append(row)

    for memseg in lines[:i]:
        [x, y] = memseg.split(",")
        map[int(y)][int(x)] = "#"

    if not search((0, 0)):
        print(lines[len(lines) - 1])
        t = i
    else:
        b = i

print(lines[t-1])