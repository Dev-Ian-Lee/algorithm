# <이것이 취업을 위한 코딩 테스트다> 예제 5-6

from collections import deque

def bfs(graph, root, visited):
    queue = deque([root])
    visited[root] = True

    while queue:
        node = queue.popleft()
        print(node, end = ' ')

        for adjacent in graph[node]:
            if not visited[adjacent]:
                queue.append(adjacent)
                visited[adjacent] = True

    print()

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * 9

bfs(graph, 1, visited)