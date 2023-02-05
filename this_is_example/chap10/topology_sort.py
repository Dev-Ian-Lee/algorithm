# <이것이 취업을 위한 코딩 테스트다> 예제 10-5

from collections import deque

V, E = map(int, input().split())

# 모든 노드의 진입차수 0으르 초기화
indegree = [0] * (V + 1)
graph = [[] for _ in range(V + 1)]

for _ in range(E):
    A, B = map(int, input().split())
    graph[A].append(B)

    # 노드 B의 진입차수 1 증가
    indegree[B] += 1

def topology_sort():
    result = []
    q = deque()

    # 먼저 진입차수가 0인 노드들을 큐에 삽입
    for i in range(1, V + 1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        curr = q.popleft()
        result.append(curr)

        # 큐에서 꺼낸 현재 노드와 연결된 노드의 진입차수 1 차감
        for node in graph[curr]:
            indegree[node] -= 1

            # 새롭게 진입차수가 0이 된 노드를 큐에 삽입
            if indegree[node] == 0:
                q.append(node)

    for node in result:
        print(node, end = ' ')

    print()

topology_sort()