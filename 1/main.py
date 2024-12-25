# Day 1, Part 1


with open('./inp.txt') as f:
    lines = f.read().split()

left = [] 
right = [] 
flag = True
total = 0

for line in lines: 
    if flag: 
        left.append(int(line))
        flag = False
    else:
        right.append(int(line))
        flag = True

left.sort()
right.sort()

for i in range(len(left)):
    total += abs(right[i] - left[i])
print(total)

