# <이것이 취업을 위한 코딩 테스트다> 실전 문제 10-6

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])

    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a

    else:
        parent[a] = b

N, M = map(int, input().split())
parent = [0] * (N + 1)

for i in range(N + 1):
    parent[i] = i

for _ in range(M):
    op, a, b = map(int, input().split())

    if op == 0:
        union_parent(parent, a, b)

    else:
        if find_parent(parent, a) == find_parent(parent, b):
            print('YES')

        else:
            print('NO')