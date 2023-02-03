# <이것이 취업을 위한 코딩 테스트다> 예제 9-1

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
visited = [False] * (N + 1)

# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (N + 1)

# 모든 간선 정보 입력
for _ in range(M):

    # A노드에서 B노드로 가는 비용이 C
    A, B, C = map(int, input().split())
    graph[A].append((B, C))

# 방문하지 않은 노드 중에서, 최단 거리가 가장 짧은 노드의 번호를 반환
def get_smallest_node():
    min_value = INF

    # 최단 거리가 가장 짧은 노드(인덱스)
    index = 0

    for i in range(1, N + 1):
        if distance[i] < min_value and visited[i] == False:
            min_value = distance[i]
            index = i

    return index

def dijkstra(start):
    distance[start] = 0
    visited[start] = True

    for node in graph[start]:
        distance[node[0]] = node[1]

    # 시작 노드를 데외한 전체 N - 1 개의 노드에 대해 반복
    for i in range(N - 1):
        # 현재 시점에 최단 거리가 가장 짧은 노드를 구해, 방문 처리
        curr = get_smallest_node()
        visited[curr] = True

        # 현재 노드와 연결된 다른 노드에 대해 반복
        for node in graph[curr]:

            # 현재 노드를 거쳐가는 것이 거리가 더 짧을 경우, 갱신
            cost = distance[curr] + node[1]

            if cost < distance[node[0]]:
                distance[node[0]] = cost

dijkstra(start)

# 모든 노드로 가기 위한 최단 거리 출력
for i in range(1, N + 1):
    if distance[i] == INF:
        print("INFINITY")

    else:
        print(distance[i])