from random import randint

A = [randint(1,8) for _ in range(10)]
counter = [0] * max(A)
print(A)

for item in A:
    counter[item-1] += 1

A = []
for index, item in enumerate(counter):
    if item > 0:
        A += [index+1] * item 

print(A)