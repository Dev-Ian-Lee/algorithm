# <이것이 취업을 위한 코딩 테스트다> 예제 5-4

graph = [[] for _ in range(3)]

# 0번 노드와 1번 노드가 거리 7의 간선으로 연결
graph[0].append((1, 7))

# 0번 노드와 2번 노드가 거리 5의 간선으로 연결
graph[0].append((2, 5))

graph[1].append((0, 7))
graph[2].append((0, 5))

print(graph)