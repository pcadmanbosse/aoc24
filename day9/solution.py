with open("day9/input.txt") as f:
    code = f.read()

char_list = []
free_space_list = []
c = 0
while c < len(code):
    if c % 2 == 0:
        char_list.append(int(code[c]))
    else:
        free_space_list.append(int(code[c]))
    c += 1

# Part 1
j = len(char_list) - 1
i = 0
z = 1
built_list =  [0] * char_list[0]
while j>=i:
    number_of_free_elements = free_space_list[i]
    number_of_elements_to_add = char_list[j]
    number_of_elements_from_start = char_list[z]
    if number_of_elements_to_add == number_of_free_elements:
        built_list = built_list +  [j] * char_list[j]
        if z < j:
            built_list += [z] * char_list[z]
        i += 1 
        j -= 1
        z += 1
    elif number_of_elements_to_add > number_of_free_elements:
        built_list +=  [j] * number_of_free_elements
        if z < j:
            built_list +=  [z] * char_list[z]
        char_list[j] = char_list[j] - free_space_list[i]
        i += 1
        z += 1
    else: 
        built_list +=  [j] * number_of_elements_to_add
        free_space_list[i] = free_space_list[i] - char_list[j]
        j -= 1 

res = 0
for i, el in enumerate(built_list):
    res += i*el
print(res)

# Part 2
char_list = []
free_space_list = []
built_list= []
c = 0
while c < len(code):
    if c % 2 == 0:
        char_list.append(int(code[c]))
    else:
        free_space_list.append(int(code[c]))
    c += 1
j = len(char_list) - 1

free_space_add_list =[]
for i in range(len(free_space_list)):
    free_space_add_list.append([])
empty_pos_list = []
for i in range(len(char_list)):
    empty_pos_list.append(0)

while j > 0:
    done = False
    i = 0
    if char_list[j] == 0:
        continue
    while i < j and not done:
        if free_space_list[i] >= char_list[j]:
            free_space_add_list[i].append((j, char_list[j]))
            free_space_list[i] -= char_list[j]
            empty_pos_list[j] = char_list[j]
            char_list[j] = 0
            done = True
        else: 
            i = i+1
    j = j-1

for i in range(len(char_list)):
    built_list += [i] * char_list[i]
    built_list += [0] * empty_pos_list[i]

    if i < len(free_space_add_list):
        for k in free_space_add_list[i]:
            built_list += [k[0]] * k[1]
    if i < len(free_space_list):
        built_list += [0] * free_space_list[i]
   
    
res = 0
for i, el in enumerate(built_list):
    res += i*el
print(res)