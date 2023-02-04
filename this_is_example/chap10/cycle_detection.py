# <이것이 취업을 위한 코딩 테스트다> 예제 10-3

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

V, E = map(int, input().split())
parent = [0] * (V + 1)

for i in range(1, V + 1):
    parent[i] = i

cycle = False
for i in range(E):
    A, B = map(int, input().split())

    # 사이클이 발생한 경우 종료
    if find_parent(parent, A) == find_parent(parent, B):
        cycle = True

    # 사이클이 발생하지 않았다면 union 수행
    else:
        union_parent(parent, A, B)

if cycle:
    print('사이클이 발생했습니다.')

else:
    print('사이클이 발생하지 않았습니다.')