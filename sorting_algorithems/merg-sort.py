from random import randint

A = [randint(1,5)  for _ in range(10)]
print(A)

def merge(A, B):
    C = list()
    i = j = k = 0
    while i < len(A) and j < len(B):
        if A[i] < B[j]:
            C[k] = A[i]
            i += 1
            k += 1
        else:
            C[k] = A[j]
            j += 1
            k += 1
    while i < len(A):
        C[k] = A[i]
        i += 1
        k += 1
    while j < len(B):
            C[k] = A[j]
            j += 1
            k += 1
def merg_sort(A):
    if len(A) == 1:
        return A
    
    mid = len(A) // 2
    left_side = A[:mid]
    right_side = A[mid:]
    merg_sort(left_side)
    merg_sort(right_side)
    merge(left_side, right_side)

merg_sort(A)
print(A)