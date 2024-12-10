with open("day10/input.txt") as f:
    grid = [[int(y) for y in x] for x in f.read().splitlines()]

# Part 1
def is_valid_candidate(coords, prev_val, path):
    return coords[0] >= 0 and coords[0] < len(grid) and coords[1] >= 0 and coords[1] < len(grid[0]) and \
    grid[coords[0]][coords[1]] == prev_val+1 and not any(x[0] == coords[0] and x[1] == coords[1] for x in path)

def dfs(y, x,):
    queue = [(y, x, [])]
    paths = 0
    summits = set()
    while len(queue) > 0:
        next_el = queue.pop()
        next_y = next_el[0]
        next_x = next_el[1]
        path = next_el[2]
        if grid[next_y][next_x] == 9:
            paths = paths + 1
            summits.add((next_y, next_x))
            continue
        
        next_candidates = [(next_y-1, next_x), (next_y+1, next_x), (next_y, next_x-1), (next_y, next_x+1)]  
        for candidate in next_candidates:
            if is_valid_candidate(candidate, grid[next_y][next_x], path):
                queue.append((candidate[0], candidate[1], path + [(next_y, next_x)]))
    return len(summits), paths


score_part_1 = 0
score_part_2 = 0
for y, row in enumerate(grid):
    for x, _ in enumerate(row):
        if grid[y][x] == 0:
            res = dfs(y, x)
            score_part_1 += res[0]
            score_part_2 += res[1]
            
print(score_part_1)
print(score_part_2)
