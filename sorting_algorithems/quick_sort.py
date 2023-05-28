from random import randint

def quick_sort(A):
    if len(A) < 2:
        return A
    
    pivot = A[0]
    less = [i for i in A[1:] if i < pivot]
    grater = [i for i in A[1:] if i >= pivot]

    return quick_sort(less) + [pivot] + quick_sort(grater)

def quick_sort_less_RAM(A, right, left):
    if right >= left:
        return A
    pivot = left - 1
    left -= 2
    while right < left:
        while A[right] < A[pivot]:
            right+=1
        while A[left] >= A[pivot]:
            left+=1
        A[left], A[right] = A[right], A[left]
    A[left+1], A[pivot] = A[pivot], A[left+1]

    return quick_sort(A, right, left) + quick_sort(A, left + 1, pivot)
    

a = [randint(1,10) for i in range(10)]
print("Before: ")
print(a)


a = quick_sort(a)
print("After: ")
print(a)

b = quick_sort_less_RAM(a, 0, len(a))
print(b)