with open("day7/input.txt") as f:
    equations = f.read().splitlines()

def parse_equation(equation):
    left, right = equation.split(": ")
    left = int(left)
    right = [int(x) for x in right.split(" ")]
    return left, right

def check_equation(equation):
    left, right = parse_equation(equation)
    results = set()
    queue = [(right[0], 1)]
    while len(queue) > 0:
        value, index = queue.pop()
        if index == len(right):
            results.add(value)
        else:
            next_value = right[index]
            queue.append((value + next_value, index + 1))
            queue.append((value * next_value, index + 1))
    if left in results:
        return left
    return 0

# Part 1
count = 0
for equation in equations:
    count += check_equation(equation)

# Part 2
def check_equation(equation):
    left, right = parse_equation(equation)
    results = set()
    queue = [(right[0], 1)]
    while len(queue) > 0:
        value, index = queue.pop()
        if index == len(right):
            results.add(value)
        else:
            next_value = right[index]
            queue.append((value + next_value, index + 1))
            queue.append((value * next_value, index + 1))
            queue.append((int(str(value)+str(next_value)), index+1))
    if left in results:
        return left
    return 0
count = 0
for equation in equations:
    count += check_equation(equation)
print(count)
