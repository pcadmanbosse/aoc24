with open('day2/input.txt') as f:
    data = [x.split(" ") for x in f.read().splitlines()]

def is_level_safe(level):
    previous_delta = None
    safe = True
    for i in range(len(level) - 1):
        if level[i] == level[i+1] or \
            (int(level[i]) > int(level[i+1]) and previous_delta == "increasing") \
                or (int(level[i]) < int(level[i+1]) and previous_delta == "decreasing"):
            safe = False
            break
        if abs(int(level[i]) - int(level[i+1])) > 3:
            safe = False
            break
        previous_delta = "increasing" if int(
            level[i]) < int(level[i+1]) else "decreasing"
    return safe
# Part 1
number_of_safe_levels = 0
for level in data:
     if is_level_safe(level):
        number_of_safe_levels += 1
print(number_of_safe_levels)

# Part 2
# Brute force
number_of_safe_levels = 0
for level in data:
    combinations = []
    for i in range(len(level)):
        combinations.append([*level[0:i],*level[i+1:]])
    if any([is_level_safe(x) for x in combinations]):
        number_of_safe_levels += 1
            
print(number_of_safe_levels)