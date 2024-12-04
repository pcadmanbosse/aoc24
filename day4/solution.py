with open("day4/input.txt") as f:
    grid = [[y for y in x] for x in f.read().splitlines()]

# Part 1
order = ["X", "M", "A", "S"]
x_len = len(grid[0])
y_len = len(grid)
def navigate(x, y, index, delta=None):
    if x < 0 or x >= x_len or y < 0 or y >= y_len:
        return 0
    if grid[y][x] == order[index]:
        if index == len(order) - 1:
            return 1
        if delta != None:
            if delta == (1, 0):
                return navigate(x + 1, y, index + 1, delta)
            elif delta == (-1, 0):
                return navigate(x - 1, y, index + 1, delta)
            elif delta == (0, 1):
                return navigate(x, y + 1, index + 1, delta)
            elif delta == (0, -1):
                return navigate(x, y - 1, index + 1, delta)
            elif delta == (1, 1):
                return navigate(x + 1, y + 1, index + 1,delta)
            elif delta == (1, -1):
                return navigate(x + 1, y - 1, index + 1,delta)
            elif delta == (-1, 1):
                return navigate(x - 1, y + 1, index + 1, delta)
            elif delta == (-1, -1):
                return navigate(x - 1, y - 1, index + 1, delta)
        return (
            navigate(x - 1, y, index + 1, (-1, 0))
            + navigate(x + 1, y, index + 1, (1, 0))
            + navigate(x, y - 1, index + 1, (0, -1))
            + navigate(x, y + 1, index + 1, (0, 1))
            + navigate(x - 1, y - 1, index + 1, (-1, -1))
            + navigate(x - 1, y + 1, index + 1, (-1, 1))
            + navigate(x + 1, y - 1, index + 1, (1, -1))
            + navigate(x + 1, y + 1, index + 1, (1, 1))
        )
    return 0


xmases = 0
for y in range(y_len):
    for x in range(x_len):
        xmases += navigate(x, y, 0)
print(xmases)

# Part 2
def is_mas(a,c):
    return (a == "M" and c == "S") or (a == "S" and c == "M")

xmases = 0
for y in range(1, y_len -1):
    for x in range(1, x_len -1):
        if grid[y][x] == "A":
            if is_mas(grid[y-1][x-1], grid[y+1][x+1]) and is_mas(grid[y-1][x+1], grid[y+1][x-1]):
                xmases += 1
print(xmases)
