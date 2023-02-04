# <이것이 취업을 위한 코딩 테스트다> 실전 문제 9-5

import heapq
import sys
input = sys.stdin.readline

INF = int(1e9)

N, M, C = map(int, input().split())
start = C

graph = [[] for _ in range(N + 1)]
distance = [INF] * (N + 1)

for _ in range(M):
    X, Y, Z = map(int, input().split())
    graph[X].append((Y, Z))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, curr = heapq.heappop(q)

        if distance[curr] < dist:
            continue

        for node in graph[curr]:
            cost = dist + node[1]

            if cost < distance[node[0]]:
                distance[node[0]] = cost
                heapq.heappush(q, (cost, node[0]))

dijkstra(start)
cities = [i for i in distance if i != INF and i!= 0]
print(len(cities), max(cities))