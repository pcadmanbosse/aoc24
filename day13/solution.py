import re
import numpy as np

with open("day13/input.txt") as f:
    raw = f.read().split("\n\n")
    regex = r"""Button A: X\+([0-9]+), Y\+([0-9]+)\nButton B: X\+([0-9]+), Y\+([0-9]+)\nPrize: X=([0-9]+), Y=([0-9]+)"""
    problems = []
    for r in raw:
        match = re.match(regex, r, re.M)
        problems.append(
            (
                int(match[1]),
                int(match[2]),
                int(match[3]),
                int(match[4]),
                int(match[6]),
                int(match[5]),
            )  # ax, ay, bx, by, targetx, targety = problem
        )
cost_A = 3
cost_B = 1

total_cost = 0
def is_whole(f, eps):
    return abs(f - round(f)) < abs(eps)

# Part 1:
for problem in problems:
    ax, ay, bx, by, targetx, targety = problem
    M = np.array([[ax, bx], [ay, by]])

    T = np.array((targety, targetx))
    # det = np.linalg.det(M)
    # handle det
    [a_times, b_times] = np.linalg.solve(M, T)
    if a_times >= 101 or b_times >= 101 or a_times < 0 or b_times < 0:
        # print("too large")
        # print(a_times, b_times)
        continue
    elif not is_whole(a_times, 0.00000001) or not is_whole(b_times, 0.00000001):
        # print("not integer")
        # print(a_times, b_times)
        continue
    else:
        total_cost += round(a_times) * 3
        total_cost += round(b_times)

print(total_cost)

total_cost = 0
# Part 2:
for problem in problems:
    ax, ay, bx, by, targetx, targety = problem
    M = np.array([[ax, bx], [ay, by]])
    T = np.array((targety + 10000000000000, targetx + 10000000000000))
    [a_times, b_times] = np.linalg.solve(M, T)
    if a_times < 0 or b_times < 0:
        continue
    elif not is_whole(a_times, 0.0001) or not is_whole(b_times, 0.001):
        continue
    else:
        total_cost += round(a_times) * 3
        total_cost += round(b_times)

print(total_cost)