import random

A = [random.randint(1, 8) for _ in range(10)]

print(A)
had_boubble = False

for _ in range(len(A) - 1):
    for index in range(len(A) - 1):
        if A[index] > A[index + 1] :
            had_boubble = True
            A[index] , A[index + 1] = A[index + 1], A[index]
    if not had_boubble:
        break
print(A)
