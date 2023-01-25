import random

A = [random.randint(1, 8) for _ in range(10)]
print(A)

for i in range(1, len(A)):
    temp = A[i]
    while temp < A[i - 1] and i > 0:
        A[i] = A[i-1]
        i -= 1
    A[i] = temp

print(A)