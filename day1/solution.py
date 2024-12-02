with open('day1/input.txt') as f:
    data = [x.split("   ") for x in f.read().splitlines()]

l1 = sorted([int(x[0]) for x in data])
l2 = sorted([int(x[1]) for x in data])

# Part 1 
print(sum([abs(i-j) for i,j in zip(l1,l2)]))

# Part 2 
count_map = {}
for i in l2:
    count_map[i] = count_map.get(i, 0) + 1

score = 0
for i in l1:
    score += i * count_map.get(i, 0)
print(score)