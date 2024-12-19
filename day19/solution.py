import functools
import itertools

with open("day19/input.txt") as f:
    parts = f.read().split("\n\n")
    stock = [x for x in parts[0].split(", ")]
    patterns = parts[1].split("\n")


# Part 1
possible_patterns = set(stock)
count = 0
patterns.sort(key=lambda x: len(x))


def find_pattern(starting_pattern) -> int:
    queue = [0]
    searched = set()
    while len(queue) > 0:
        pattern_search_index = queue.pop()
        if pattern_search_index == len(starting_pattern):
            return 1
        pattern = starting_pattern[pattern_search_index:]
        if pattern in possible_patterns:
            return 1
        if pattern_search_index not in searched:
            searched.add(pattern_search_index)
            for stock_element in stock:
                if stock_element == pattern[: len(stock_element)]:
                    possible_patterns.add(
                        starting_pattern[: pattern_search_index + len(stock_element)]
                    )
                    queue.append(pattern_search_index + len(stock_element))
    return 0


for pattern in patterns:
    count += find_pattern(pattern)

print(count)

# Part 2
@functools.cache
def find_pattern_combinations(pattern):
    combinations = 0
    for s in stock:
        if s == pattern:
            combinations = combinations + 1
        elif pattern.startswith(s):
            combinations += find_pattern_combinations(pattern[len(s):])
    return combinations

count = 0
for pattern in patterns: 
    count += find_pattern_combinations(pattern)
    print(count)
print(count)