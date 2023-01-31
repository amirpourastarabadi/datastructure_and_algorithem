from random import randint

A = [randint(0,9)  for _ in range(10)]
print(A)

def merg_sort(A):
    if len(A) == 1:
        return A

    mid = len(A) // 2

    left_side = merg_sort(A[:mid])
    right_side = merg_sort(A[mid:])
    return merge(left_side, right_side)

def merge(B, C):
    A = []
    i = j = 0

    while i < len(B) and j < len(C):
        if B[i] < C[j]:
            A += [B[i]]
            i += 1
        else:
            A  += [C[j]]
            j += 1
    A += B[i:] + C[j:]
    return A

A = merg_sort(A)
print(A)

