import networkx as nx

with open("day23/input.txt") as f:
    connections = f.read().split("\n")

graph = nx.Graph()
for conn in connections:
    [f, t] = conn.split("-")
    graph.add_edge(f, t, weight=-1)

# Part 1
total = 0
for cycle in nx.simple_cycles(graph, length_bound=3):
    if any([x.startswith("t") for x in cycle]):
        total += 1
print(total)
# Part 2
print(",".join(sorted(sorted(nx.find_cliques(graph), key=lambda x: len(x))[-1])))
