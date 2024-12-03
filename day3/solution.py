import re


with open('day3/input.txt') as f:
    data = f.read()

# Part 1 
pattern = r"mul\((\d+,\d+)\)"
sum = 0
for match in re.findall(pattern, data):
    sum += int(match.split(',')[0]) * int(match.split(',')[1])
print(sum)

# Part 2
pattern = r"(mul\((\d+,\d+)\)|do\(\)|don't\(\))"
sum = 0
add = True
for match in re.findall(pattern, data):
    if "mul" in match[0] and add:
        sum += int(match[1].split(',')[0]) * int(match[1].split(',')[1])
    elif "do()" in match[0]:
        add = True
    elif "don't()" in match[0]:
        add = False
print(sum)