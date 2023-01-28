from random import randint

A = [randint(1,6) for _ in range(10)]

print(A)
n = len(A)

for i in range(n - 1):
    min_index = i
    for j in range(i, n):
        if A[min_index] > A[j]:
            min_index = j
    A[min_index], A[i] = A[i], A[min_index]

print(A)