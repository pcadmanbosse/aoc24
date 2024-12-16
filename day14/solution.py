import re
import matplotlib.pyplot as plt
import numpy as np
import numpy as np
from scipy.stats import entropy

with open("day14/input.txt") as f:
    raw = f.read().splitlines()
    robots = []
    regex = r"p=([0-9]+),([0-9]+) v=(-?[0-9]+),(-?[0-9]+)"
    for row in raw:
        match = re.match(regex, row)
        robots.append((int(match[1]), int(match[2]), int(match[3]), int(match[4])))


# Part 1
map = {}
wide = 101
tall = 103

for robot in robots:
    x, y, dx, dy = robot
    final_x = (x + 100*dx) % wide
    final_y = (y + 100*dy) % tall

    map[final_y] = map.get(final_y, {})
    map[final_y][final_x] = map[final_y].get(final_x, 0) + 1
    
quadrants = [0, 0, 0, 0]

for y in map:
    for x in map[y]:
        # bottom right
        if y > tall//2 and y < tall and x > wide//2 and x < wide:
            quadrants[3] += map[y][x]
        # top right
        elif y < tall//2 and x > wide//2 and x < wide:
            quadrants[1] += map[y][x]
        # top left
        elif y < tall//2 and x < wide//2:
            quadrants[0] += map[y][x]
        # bottom left
        elif y > tall//2 and x<wide//2:
            quadrants[2] += map[y][x]

r = 1
for quadrant in quadrants:
    r = r*quadrant
print(r)

# Part 1
wide = 101
tall = 103

entropies = []
for z in range(0, 10000):
    map = {}
    for robot in robots:
        x, y, dx, dy = robot
        final_x = (x + z*dx) % wide
        final_y = (y + z*dy) % tall

        map[final_y] = map.get(final_y, {})
        map[final_y][final_x] = map[final_y].get(final_x, 0) + 1
        
    quadrants = [0, 0, 0, 0]
    for y in map:
        for x in map[y]:
            # bottom right
            if y > tall//2 and y < tall and x > wide//2 and x < wide:
                quadrants[3] += map[y][x]
            # top right
            elif y < tall//2 and x > wide//2 and x < wide:
                quadrants[1] += map[y][x]
            # top left
            elif y < tall//2 and x < wide//2:
                quadrants[0] += map[y][x]
            # bottom left
            elif y > tall//2 and x<wide//2:
                quadrants[2] += map[y][x]

    r = 1
    for quadrant in quadrants:
        r = r*quadrant
    entropies.append(r)

# Data for plotting
t = range(len(entropies))
s = entropies

fig, ax = plt.subplots()
ax.plot(t, s)

ax.set(xlabel='time (s)', ylabel='Entropy',
       title='Entropy')
ax.grid()

fig.savefig("day14/entropies.png")
plt.show()