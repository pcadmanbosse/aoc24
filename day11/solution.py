with open("day11/input.txt") as f:
    og_stones = [int(x) for x in f.read().split(" ")]

# Part 1
stones = og_stones
for i in range(25):
    new_stones = []
    for stone in stones:
        stone_str = str(stone)
        if stone == 0:
            new_stones.append(1)
        elif len(stone_str) % 2 == 0:
            new_stones.append(int(stone_str[0 : len(stone_str) // 2]))
            new_stones.append(int(stone_str[len(stone_str) // 2 :]))
        else:
            new_stones.append(2024 * stone)
    stones = new_stones
print(len(stones))

# Part 2
stones = og_stones
stone_order_map = {}
stone_count_map = {}

def populate(stone):
    if not stone in stone_order_map:
        if stone == 0:
            stone_order_map[stone] = [1]
        else:
            stone_str = str(stone)
            if len(stone_str) % 2 == 0:
                stone_order_map[stone] = [
                    int(stone_str[0 : len(stone_str) // 2]),
                    int(stone_str[len(stone_str) // 2 :]),
                ]
            else:
                stone_order_map[stone] = [2024 * stone]

i = 75
while i >= 0:
    new_stones = []
    for stone in stones:
        if stone not in stone_order_map:
            populate(stone)
            for x in stone_order_map[stone]:
                new_stones.append(x)
    stones = new_stones
    i = i-1

i = 74
while i >= 0:
    for key in stone_order_map:
        if i == 74:
            stone_count_map[key] = {i: len(stone_order_map[key])}
        else: 
            count = 0
            for next in stone_order_map[key]:
                count = count + stone_count_map[next][i+1]
            stone_count_map[key][i] = count
    i = i-1

count = 0
for stone in og_stones:
    count = count+stone_count_map[stone][0]
print(count)

