codes = ["869A", "180A", "596A", "965A", "973A"]
codes = [
    "029A",
    "980A",
    "179A",
    "456A",
    "379A",
]

digit_graph = {
    "0": {"up": "2", "right": "A"},
    "A": {"left": "0", "up": "3"},
    "1": {"up": "4", "right": "2",},
    "2": {"left": "1", "right": "3", "up": "5", "down": "0"},
    "3": {"left": "2", "up": "6", "down": "A"},
    "4": {"down": "1", "right": "5", "up": "7"},
    "5": {"left": "4", "right": "6", "up": "8", "down": "2"},
    "6": {"left": "5", "up": "9", "down": "3"},
    "7": {"down": "4", "right": "8"},
    "8": {"left": "7", "down": "5", "right": "9"},
    "9": {"left": "8", "down": "6"},
}

directional_graph = {
    "up": {"right": "A", "down": "down"},
    "down": {"up": "up", "left": "left", "right": "right"},
    "left": {
        "right": "down",
    },
    "right": {"left": "down", "up": "A"},
    "A": {"left": "up", "down": "right"},
}

costs = {
"A":{
    "up": 2,
    "right": 2,
    "left": 6,
    "down": 4,
    "A": 0
},
"up": {
    "up": 0,
    "down": 2,
    "A": 2,
    "right": 4,
    "left": 4
},
"right": {
    "A": 2,
    "down": 2,
    "up": 4,
    "left": 4,
    "right": 0
}, 
"left": {
    "down": 2,
    "up": 4,
    "right": 4,
    "A": 6,
    "left": 0
}, 
"down": {
    "up": 2,
    "down": 0,
    "right": 2,
    "left": 2,
    "A": 4
}
}

def calc_cost(path, ind):
    if ind == 2: 
        return len(path)
    return sum([costs["A"][x] for x in path])

# Part 1
def search_find(search_code, graph, ind):
    insts = []
    # code element by code element
    for y, code in enumerate(search_code):
        best_code = len(search_code)**len(search_code)
        cb = []
        starting_graph_pos = "A" if y == 0 else search_code[y-1]
        queue = []
        queue.append((starting_graph_pos, [], []))

        while len(queue) > 0:
            (el, path, visited) = queue.pop()
            if el == code:
                cost = calc_cost(insts + path + ["A"], ind)
                if cost < best_code:
                    best_code = cost
                    cb = path + ["A"]
            else:
                for key in graph[el].keys():
                    if graph[el][key] != el and graph[el][key] not in visited:
                        queue.append((graph[el][key], path + [key], visited + [el]))
        insts.extend(cb)
    return insts

#<vA<AA>>^AvAA<^A>A<v<A>>^AvA^A<vA>^A<v<A>^A>AAvA^A<v<A>A>^AAAvA<^A>A
#v<<A>>^A<A>AvA<^AA>A<vAAA>^A
#<A^A>^^AvvvA

#<v<A>>^AAAvA^A<vA<AA>>^AvAA<^A>A<v<A>A>^AAAvA<^A>A<vA>^A<A>A
#v<<A>>^AAAvA^Av<A<AA>>^AvAA^<A>Av<A>^Av<<A>>^AAAv<<A>>^AvAA^<A>Av<A>^A<A>A
total = 0
for code in codes:
    numeric = int(code[0:3])
    st_code = search_find(code, digit_graph, 0)
    print(''.join(st_code).replace("down", "v").replace("left", "<").replace("right", ">").replace("up", "^"))
    for i in range(0, 2):
        st_code = search_find(st_code, directional_graph, i+1)
    print(''.join(st_code).replace("down", "v").replace("left", "<").replace("right", ">").replace("up", "^"))
    print(len(st_code))
    total += len(st_code) * numeric

print(total)


# l --> r
# A --> x --> y --> l --> x --> y --> A