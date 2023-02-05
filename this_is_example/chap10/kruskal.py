# <이것이 취업을 위한 코딩 테스트다> 예제 10-4

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

# 모든 간선을 담을 리스트와 최종 비용을 담을 변수
edges = []
result = 0

for _ in range(E):
    A, B, cost = map(int, input().split())
    edges.append((cost, A, B))

edges.sort()

for edge in edges:
    cost, a, b = edge

    # 사이클이 발생하지 않는 경우에만 간선을 집합에 포함
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(result)