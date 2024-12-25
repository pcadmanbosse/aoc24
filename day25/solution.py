with open("day25/input.txt") as f:
    locks_and_keys = f.read().split("\n\n")
    locks = []
    keys = []
    for c in locks_and_keys:
        to_m = [[x for x in y] for y in c.split("\n")]
        if to_m[0] == ["#", "#", "#", "#", "#"]:
            locks.append(to_m)
        else:
            keys.append(to_m)

l_s = []
for l in locks:
    vals = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0}
    for r in l[1:6]:
        for i, y in enumerate(r):
            if y == "#":
                vals[i] = vals[i] + 1
    l_s.append(vals)

k_s = []
for l in keys:
    vals = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0}
    for r in l[1:6]:
        for i, y in enumerate(r):
            if y == "#":
                vals[i] = vals.get(i, 0) + 1
    k_s.append(vals)

matches = 0
leftovers = []
for lock in l_s:
    has_match = False
    for key in k_s:
        valid = True
        for ind in lock:
            if (lock[ind] + key[ind]) > 5:
                valid = False
        if valid:
            matches+=1


print(matches)
