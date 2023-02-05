# <이것이 취업을 위한 코딩 테스트다> 실전 문제 10-8

from collections import deque

def topology_sort():
    q = deque()
    result = cost[0:]
    
    for i in range(1, N + 1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        curr = q.popleft()

        for node in graph[curr]:
            indegree[node] -=1
            result[node] = max(result[node], result[curr] + cost[node])

            if indegree[node] == 0:
                q.append(node)

    for i in range(1, N + 1):
        print(result[i])

N = int(input())

cost = [0] * (N + 1)
graph = [[] for _ in range(N + 1)]
indegree = [0] * (N + 1)

for i in range(1, N + 1):
    info = list(map(int, input().split()))
    cost[i] = info[0]

    if len(info) >= 3:
        nodes = info[1:-1]

        for node in nodes:
            graph[node].append(i)

        indegree[i] += len(nodes)

topology_sort()