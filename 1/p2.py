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

for num in left:
    total += (right.count(num) * num)
print(total)