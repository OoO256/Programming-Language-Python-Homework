A =  [[1, 2, 3], [4, 5], [1, 3, 5, 7], [1, 1, 1, 1, 1]]

print('original A :', A)

for i in range(len(A)):
    ssum = 0
    for j in A[i]:
        ssum += j*j
    A[i] = ssum

print('changed A :', A)
