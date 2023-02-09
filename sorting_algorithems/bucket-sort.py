from random import randint

def selection_sort(LIST):
    n = len(LIST)

    for i in range(n - 1):
        min_index = i
        for j in range(i, n):
            if LIST[min_index] > LIST[j]:
                min_index = j
        LIST[min_index], LIST[i] = LIST[i], LIST[min_index]
    
    return LIST

A = [randint(1,20) for _ in range(20)]
print(A)

buckets = [[] for _ in range(10)]

for i in A:
    buckets[i // 10] += [i]

A = []
for l in buckets:
    A += selection_sort(l);

print(A)



