from random import randint

def quick_sort(A):
    if len(A) < 2:
        return A
    
    pivot = A[0]
    less = [i for i in A[1:] if i < pivot]
    grater = [i for i in A[1:] if i >= pivot]

    return quick_sort(less) + [pivot] + quick_sort(grater)

a = [randint(1,10) for i in range(10)]
print("Before: ")
print(a)


a = quick_sort(a)
print("After: ")
print(a)
