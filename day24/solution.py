import re
import networkx as nx 

with open("day24/input.txt") as f:
    [gates, insts] = f.read().split("\n\n")
    gates = gates.split("\n")
    insts = insts.split("\n")

status = {}

for gate in gates:
    [g, op] = gate.split(": ")
    status[g] = True if op == "1" else False


def process(a, b, op):
    if op == "OR":
        return a or b
    if op == "AND":
        return a and b
    if op == "XOR":
        return a != b
    
r = r"(.*) (AND|OR|XOR) (.*) -> (.*)"
while len(insts) > 0:
    inst = insts.pop(0)
    patts = re.match(r, inst)
    a = patts[1]
    op = patts[2]
    b = patts[3]
    result_loc = patts[4]
    if (a not in status) or (b not in status):
        insts.append(inst)
        continue
    status[result_loc] = process(status[a], status[b], op)

bits = []
for k in reversed(sorted([k for k in status.keys() if k.startswith("z")])):
    print(k)
    bits.append(1 if status[k] else 0)

print(''.join([str(x) for x in bits]))
print(int(''.join([str(x) for x in bits]), 2))


# Part 2:
graph = nx.DiGraph()
for inst in insts:
    patts = re.match(r, inst)
    a = patts[1]
    op = patts[2]
    b = patts[3]
    result_loc = patts[4]
    graph.add_edge(a, b, op)

nx.draw(graph)