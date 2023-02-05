# <이것이 취업을 위한 코딩 테스트다> 실전 문제 10-7

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

edges = []
result = 0

for _ in range(M):
    A, B, C = map(int, input().split())
    edges.append((C, A, B))

edges.sort()
last = 0

for edge in edges:
    cost, a, b = edge

    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
        last = cost
        
print(result - last)