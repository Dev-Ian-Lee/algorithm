# <이것이 취업을 위한 코딩 테스트다> 예제 9-2

import heapq
import sys
input = sys.stdin.readline

# 무한을 의미하는 값으로 10억을 설정
INF = int(1e9)

# 노드의 개수, 간선의 개수 입력
N, M = map(int, input().split())

# 시작 노드 번호 입력
start = int(input())

# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트
graph = [[] for i in range(N + 1)]

# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (N + 1)

# 모든 간선 정보 입력
for _ in range(M):

    # A노드에서 B노드로 가는 비용이 C
    A, B, C = map(int, input().split())
    graph[A].append((B, C))

def dijkstra(start):
    q = []

    # 시작 노드 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        # 최단 거리가 가장 짧은 노드 추출
        dist, curr = heapq.heappop(q)

        # 현재 노드까지의 거리가 추출한 노드까지의 거리보다 짧다면 스킵
        if distance[curr] < dist:
            continue

        for node in graph[curr]:
            cost = dist + node[1]

            if cost < distance[node[0]]:
                distance[node[0]] = cost
                heapq.heappush(q, (cost, node[0]))

dijkstra(start)

# 모든 노드로 가기 위한 최단 거리 출력
for i in range(1, N + 1):
    if distance[i] == INF:
        print("INFINITY")

    else:
        print(distance[i])