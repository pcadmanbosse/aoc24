with open("day5/input.txt") as f:
    data = f.read()

part1 = data.split("\n\n")[0]
part2 = data.split("\n\n")[1]
orders = part1.split("\n")
commands = part2.split("\n")

number_of_elements = len(orders) * 2
ordering = []
ordering_map = {}
reverse_ordering_map = {}
for order in orders:
    before = order.split("|")[0]
    after = order.split("|")[1]
    ordering_map[before] = ordering_map.get(before, []) + [after]
    ordering = ordering + [before, after]
    reverse_ordering_map[after] = reverse_ordering_map.get(after, []) + [before]

# Part 1
score = 0
for command in commands:
    things_that_cant_be_now = set()
    els = command.split(",")
    valid = True
    for el in els:
        if el in things_that_cant_be_now:
            valid = False
        elif el in reverse_ordering_map:
            things_that_cant_be_now |= set(reverse_ordering_map[el])
    if valid:
        score += int(els[int(len(els) // 2)])


print(score)

# Part 2:
def compute_score(nodes, edges):
    # Transitive reduction
    for edge in edges:
        for edge_to in edges:
            for edge_descendant in edges:
                if edge_descendant in edges[edge] and edge_descendant in edges[edge_to] and edge_to in edges[edge]:
                    edges[edge].remove(edge_descendant)
    queue = []
    for node in nodes:
        queue.append((node, []))
        while len(queue) > 0 :
            next_node, path = queue.pop(0)
            if len(path) == len(nodes) - 1:
                path.append(next_node)
                return int(path[len(nodes) // 2])

            if next_node in edges:
                for child in edges[next_node]:
                    queue.append((child, path + [next_node]))

score = 0
for command in commands:
    things_that_cant_be_now = set()
    els = command.split(",")
    nodes = set(els)
    edges = {}
    valid = True
    for el in els:
        nodes.add(el)
        if el in things_that_cant_be_now:
            valid = False
        valid_edges_for_el = nodes - set([el])
        if el in reverse_ordering_map:
            things_that_cant_be_now |= set(reverse_ordering_map[el])
            valid_edges_for_el = valid_edges_for_el - set(reverse_ordering_map[el])
        edges[el] = set(valid_edges_for_el) 
    if not valid:
        score += compute_score(nodes, edges)
print(score)
