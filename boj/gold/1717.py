# https://www.acmicpc.net/problem/1717

# 걸린 시간: -
# 시간복잡도: O(M * log N)

# n * m이 최대 1000억이기 때문에 O(N * M)이면 시간초과 발생
# union-find 유형이라는 건 알았는데 구현 방법이 생각나지 않아서 검색
# find 연산은 재귀적으로 동작하기 때문에 O(log N), union 연산은 부모 찾는 과정 제외하고 합치는 것만 고려하면 O(1)

import sys
sys.setrecursionlimit(10**6)

n, m = map(int, sys.stdin.readline().split())
parent = [i for i in range(n + 1)]

# 루트 노드 탐색
def find(a):
    if a == parent[a]:
        return a
    
    # 부모 노드 재귀적으로 탐색해 루트 노드 찾기
    tmp = find(parent[a])
    parent[a] = tmp
    return tmp
    
# a 노드의 집합과 b 노드의 집합 합치기
def union(a, b):
    a = find(a)
    b = find(b)
    
    # 두 노드의 루트 노드가 같을 경우 같은 집합
    if a == b:
        return
    
    # 루트 노드 값이 다를 경우, 더 작은 값을 부모로 설정
    if a < b:
        parent[b] = a
        
    else:
        parent[a] = b

for _ in range(m):
    op, a, b = map(int, sys.stdin.readline().split())
    
    if op == 0:
        union(a, b)
        
    else:
        if find(a) == find(b):
            print("YES")
            
        else:
            print("NO")

# 이전 코드 #2(틀림)
# 부모값을 계속 타고 확인해야하는데 이 코드는 한 번만 확인함
# import sys

# n, m = map(int, sys.stdin.readline().split())
# parent = [i for i in range(n + 1)]

# for _ in range(m):
#     op, a, b = map(int, sys.stdin.readline().split())
    
#     if op == 0:
#         if a <= b:
#             parent[b] = parent[a]
            
#         else:
#             parent[a] = parent[b]
            
#     elif op == 1:
#         if parent[a] == parent[b]:
#             print("YES")
            
#         else:
#             print("NO")

# 이전 코드 #1(시간초과)
# import sys

# n, m = map(int, sys.stdin.readline().split())

# ls = []
# for _ in range(m):
#     op, a, b = map(int, sys.stdin.readline().split())
    
#     if op == 0:
#         if len(ls) == 0:
#             ls.append(set([a, b]))
#             continue
        
#         cnt = 0
#         for ele in ls:
#             if a in ele or b in ele:
#                 ele.add(a)
#                 ele.add(b)
#                 break
            
#             cnt += 1
                
#         if cnt == len(ls):
#             ls.append(set([a, b]))
        
#     elif op == 1:
#         if len(ls) == 0:
#             print("NO")
#             continue
        
#         cnt = 0
#         for ele in ls:
#             if a in ele and b in ele:
#                 print("YES")
#                 break
            
#             cnt += 1
                
#         if cnt == len(ls):
#             print("NO")
