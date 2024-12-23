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
    best_path = None
    best_cost = (1+level)**10000
    while len(queue) > 0:
        (el, path, visited) = queue.pop()
        if el == t:
            path += ["A"]
            if level < max_level:
                res = [sequence(path[x-1] if x > 0 else "A", path[x], max_level, level+1) for x, _  in enumerate(path)]
                res = [x for y in res for x in y]
            else:
                res = path
            cost = len(res)
            if cost < best_cost:
                best_path = res
                best_cost = cost
        else:
            for key in graph[el].keys():
                if graph[el][key] != el and graph[el][key] not in visited:
                    queue.append((graph[el][key], path + [key], visited + [el]))
    if best_path == None:
        print(f, t, level)
        raise Exception("Bug")
    return best_path

# 0
#v<A<AA>>^AvAA^<A>Av<<A>>^AvA^Av<<A>>^AAv<A>A^A<A>Av<A<A>>^AAAvA^<A>A
#<vA<AA>>^AvAA<^A>A<v<A>>^AvA^A<vA>^A<v<A>^A>AAvA^A<v<A>A>^AAAvA<^A>A
#v<<A>>^A<A>AvA<^AA>A<vAAA>^A
#<A^A>^^AvvvA

# expected
#              9                 8                 0         A
#        ^^^   A         <       A        vvv      A     >   A
#    <   AAA > A  v <<   A >>  ^ A   < v  AAA >  ^ A  v  A ^ A
# <v<A>>^AAAvA^A<vA<AA>>^AvAA<^A>A<v<A>A>^AAAvA<^A>A<vA>^A<A>A

# mine
#    <   AAA > A  v <<   A >>  ^ A  v  A   <   AAA   <   A >>  ^ A 
# v<<A>>^AAAvA^Av<A<AA>>^AvAA^<A>Av<A>^Av<<A>>^AAAv<<A>>^AvAA^<A>Av<A>^A<A>A
# 980A
total = 0
for code in codes:
    int_part = int(code[0:3])
    r = []
    for i,c in enumerate(code):
        # Part 1
        # print(sequence(code[i-1] if i > 0 else "A", c, 0, 0))
        r.extend(sequence(code[i-1] if i > 0 else "A", c, 24, 0))
    # print("".join(r))
    # print(len(r))
    total += int_part * len(r)
print(total)

print(sequence("8", "0", 0, 0))