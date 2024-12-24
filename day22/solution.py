import functools


with open("day22/input.txt") as f:
    secrets = [int(s) for s in f.readlines()]

# Part 1
@functools.cache
def mix(n1, n2):
    return n1^n2
@functools.cache
def prune(n1):
    return n1%16777216

@functools.cache
def mul_1(secret):
    return 64* secret

@functools.cache
def div_1(secret):
    return secret//32

@functools.cache
def mul_2(secret):
    return 2048*secret

@functools.cache
def next_secret(secret):
    temp = mul_1(secret)
    mixed = mix(secret, temp)
    pruned = prune(mixed)
    temp_2 = div_1(pruned)
    mixed_2 = mix(pruned, temp_2)
    pruned_2 = prune(mixed_2)
    res_2 = mul_2(pruned_2)
    mixed_3 = mix(res_2, pruned_2)
    return prune(mixed_3)

s_by_s = []
for i in range(len(secrets)):
    s_by_s.append([secrets[i]%10])

for i in range(2000):
    for i, _ in enumerate(secrets):
        secrets[i] = next_secret(secrets[i])
        s_by_s[i].append(secrets[i]%10)


print(sum(secrets))

# Part 2
delta_to_banana_for_all_monkeys = {}

for i in range(len(s_by_s)):
    # print(f"{100*i/len(s_by_s)}%")
    delta_to_banana_for_this_monkey = {}
    final_digits = s_by_s[i]
    for y in range(4, len(final_digits)):
        a = final_digits[y-3] - final_digits[y-4]
        b = final_digits[y-2] - final_digits[y-3]
        c = final_digits[y-1] - final_digits[y-2]
        d = final_digits[y] - final_digits[y-1]
        if (a,b,c,d) not in delta_to_banana_for_this_monkey:
            delta_to_banana_for_this_monkey[(a,b,c,d)] = final_digits[y]
    for key in delta_to_banana_for_this_monkey:
        delta_to_banana_for_all_monkeys[key] = delta_to_banana_for_all_monkeys.get(key, 0) + delta_to_banana_for_this_monkey[key]
    
# bounded 1525 - 1605
print(max(delta_to_banana_for_all_monkeys.values()))