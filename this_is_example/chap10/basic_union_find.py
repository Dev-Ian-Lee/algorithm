# <이것이 취업을 위한 코딩 테스트다> 예제 10-1

# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 현재 노드가 루트 노드가 아닐 경우, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        return find_parent(parent, parent[x])
    
    return x

# 두 원소가 속한 집합 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a

    else:
        parent[a] = b

V, E = map(int, input().split())
parent = [0] * (V + 1)

# 자기 자신을 부모로 초기화
for i in range(1, V + 1):
    parent[i] = i

for i in range(E):
    A, B = map(int, input().split())
    union_parent(parent, A, B)

print('각 원소가 속합 집합: ', end = '')
for i in range(1, V + 1):
    print(find_parent(parent, i), end = ' ')

print()

print('부모 테이블: ', end='')
for i in range(1, V + 1):
    print(parent[i], end = ' ')

print()