import copy
import random
import numpy as np
import torch.nn as nn
import torch.optim as optim
import torch
import tqdm
from sklearn.preprocessing import StandardScaler

register_A = 330760000
# register_A = 729
register_B = 0
register_C = 0
commands = [2, 4, 1, 3, 7, 5, 0, 3, 1, 4, 4, 7, 5, 5, 3, 0]
# commands = [0, 1, 5, 4, 3, 0]

# Part 1
instruction_pointer = 0


def combo(value):
    if value <= 3:
        return value
    if value == 4:
        return register_A
    if value == 5:
        return register_B
    if value == 6:
        return register_C
    else:
        raise Exception(f"Probably a bug, combo {value}")


def handle(inst, command, value, register_A, register_B, register_C, outs):
    literal = value
    match command:
        case 0:
            register_A = int(register_A / (2 ** combo(value)))
            return inst + 2, register_A, register_B, register_C, outs
        case 1:
            register_B = register_B ^ literal
            return inst + 2, register_A, register_B, register_C, outs
        case 2:
            register_B = combo(value) % 8
            return inst + 2, register_A, register_B, register_C, outs
        case 3:
            if register_A == 0:
                return inst + 2, register_A, register_B, register_C, outs
            else:
                return literal, register_A, register_B, register_C, outs
        case 4:
            register_B = register_B ^ register_C
            return inst + 2, register_A, register_B, register_C, outs
        case 5:
            outs.append(combo(value) % 8)
            return inst + 2, register_A, register_B, register_C, outs
        case 6:
            register_B = int(register_A / (2 ** combo(value)))
            return inst + 2, register_A, register_B, register_C, outs
        case 7:
            register_C = int(register_A / (2 ** combo(value)))
            return inst + 2, register_A, register_B, register_C, outs


outs = []
while instruction_pointer < len(commands) - 1:
    instruction_pointer, register_A, register_B, register_C, outs = handle(
        instruction_pointer,
        commands[instruction_pointer],
        commands[instruction_pointer + 1],
        register_A,
        register_B,
        register_C,
        outs,
    )

print(outs)
print(",".join([str(x) for x in outs]))


# Part 2
ins = []
outputs = []
start_pos = 0
bound = 1000000
min_val = 0
min_val_index = 0
max_val = 0
max_val_index = 0
curr_best =0
commands = [2, 4, 1, 3, 7, 5, 0, 3, 1, 4, 4, 7, 5, 5, 3, 0]
max_eq = 0
max_eq_pos = 0
start = [2, 4, 1, 3, 7, 5, 0, 3, 1, 4, 4, 7, 5, 5, 3, 0]
check_ind = 0
for start_pos in range(10):
    start[check_ind] = start_pos
    instruction_pointer = 0
    register_A = start_pos
    register_B = 0
    register_C = 0
    outs = []
    past = set()
    halt = False
    while (
        not halt and 
        instruction_pointer < len(commands) - 1
        and not (instruction_pointer, register_A, register_B, register_C) in past
    ):
        past.add((instruction_pointer, register_A, register_B, register_C))

        instruction_pointer, register_A, register_B, register_C, outs = handle(
            instruction_pointer,
            commands[instruction_pointer],
            commands[instruction_pointer + 1],
            register_A,
            register_B,
            register_C,
            outs,
        )
 

    value = int("".join([str(x) for x in outs])) if len(outs) > 0 else 0
    if value > max_val:
        max_val = value
        max_val_index = start_pos
    if value < min_val:
        min_val = value
        min_val_index = start_pos

    ins.append(start_pos)
    outputs.append(value)

print([2, 4, 1, 3, 7, 5, 0, 3, 1, 4, 4, 7, 5, 5, 3, 0])
print(outputs)