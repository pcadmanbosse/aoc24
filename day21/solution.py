import functools


codes = [
    "869A", "180A", "596A", "965A", "973A"
]
digit_graph = {
    "0": {"^": "2", ">": "A"},
    "A": {"<": "0", "^": "3"},
    "1": {"^": "4", ">": "2",},
    "2": {"<": "1", ">": "3", "^": "5", "v": "0"},
    "3": {"<": "2", "^": "6", "v": "A"},
    "4": {"v": "1", ">": "5", "^": "7"},
    "5": {"<": "4", ">": "6", "^": "8", "v": "2"},
    "6": {"<": "5", "^": "9", "v": "3"},
    "7": {"v": "4", ">": "8"},
    "8": {"<": "7", "v": "5", ">": "9"},
    "9": {"<": "8", "v": "6"},
}
directional_graph = {
    "^": {">": "A", "v": "v"},
    "v": {"^": "^", "<": "<", ">": ">"},
    "<": {
        ">": "v",
    },
    ">": {"<": "v", "^": "A"},
    "A": {"<": "^", "v": ">"},
}

@functools.cache
def sequence(f, t, max_level, level):
    graph = digit_graph if level == 0 else directional_graph
    queue = []
    queue.append((f, [], []))
    best_cost = (1000+level)**10000
    while len(queue) > 0:
        (el, path, visited) = queue.pop()
        if el == t:
            path += ["A"]
            if level < max_level:
                cost = sum([sequence(path[x-1] if x > 0 else "A", path[x], max_level, level+1) for x, _  in enumerate(path)])
            else:
                cost = len(path)
            if cost < best_cost:
                best_cost = cost
        else:
            for key in graph[el].keys():
                if graph[el][key] != el and graph[el][key] not in visited:
                    queue.append((graph[el][key], path + [key], visited + [el]))
    return best_cost

total = 0
for code in codes:
    int_part = int(code[0:3])
    r = 0
    for i,c in enumerate(code):
        # Part 1
        # r.extend(sequence(code[i-1] if i > 0 else "A", c, 2, 0))
        # Part 2
        r+= sequence(code[i-1] if i > 0 else "A", c, 25, 0)
    total += int_part * r
print(total)

print(sequence("A", "0", 0, 0))