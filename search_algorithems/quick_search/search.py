from random import randint

def find(a, k):
    if k > len(a):
        return 
    index = randint(0, len(a)-1)
    pivot = a[index]

    lt = [x for x in a if x < pivot]
    eq = [x for x in a if x == pivot]
    gt = [x for x in a if x > pivot]

    if k < len(lt):
        return find(lt, k)
    elif k < len(lt) + len(eq):
        return pivot
    else:
        return find(gt, k - (len(lt) + len(eq)))
    

a = [randint(0, 100) for _ in range(10)]
b = sorted(a)


for i in range(len(a)):
    founded = find(a, i)
    print("k=", i, find(a, i))
    assert founded == b[i]
