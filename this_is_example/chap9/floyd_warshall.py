# <이것이 취업을 위한 코딩 테스트다> 예제 9-3

INF = int(1e9)

# 노드의 개수, 간선의 개수 입력
N = int(input())
M = int(input())

# 모든 간선의 값을 무한으로 초기화
graph = [[INF] * (N + 1) for _ in range(N + 1)]

# 자기 자신으로 가는 비용을 0으로 초기화
for a in range (1, N + 1):
    for b in range (1, N + 1):
        if a == b:
            graph[a][b] = 0

# 모든 간선 정보 입력
for _ in range(M):
    A, B, C = map(int, input().split())
    graph[A][B] = C

# 플로이드 워셜
for k in range(1, N + 1):
    for a in range (1, N + 1):
        for b in range (1, N + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 간선 그래프 출력
for a in range(1, N + 1):
    for b in range(1, N + 1):
        if graph[a][b] == INF:
            print("INFINITY", end = " ")


        else:
            print(graph[a][b], end = " ")

    print()