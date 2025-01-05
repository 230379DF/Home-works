import random

list_1 = [3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
b = random.choice(list_1)
list_3 = []
x = 0
y = 0
for x in range(1, 21):
    for y in range(x+1, 21):
        c = x + y
        if b % c == 0:
            list_3.append(x)
            list_3.append(y)

print(b)
print(list_3)
