def same(L):
    for i in range(len(L)//2):
        if L[i] != L[len(L) - i - 1]:
            return False
    return True

A = ['a', 'b', 'c', 'c', 'b', 'a']
B = ['a', 'b', 'c', 'd', 'c', 'b', 'a']
C = ['a', 'b', 'c', 'c', 'a', 'b']
D = ['a', 'b', 'c', 'b', 'b', 'c']
E = ['a']
F = ['a', 'a']

print(same(A))
print(same(B))
print(same(C))
print(same(D))
print(same(E))
print(same(F))
