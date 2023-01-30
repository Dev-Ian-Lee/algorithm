# <이것이 취업을 위한 코딩 테스트다> 예제 5-5

def dfs(graph, node, visited):
    visited[node] = True

    print(node, end = ' ')

    for adjacent in graph[node]:
        if not visited[adjacent]:
            dfs(graph, adjacent, visited)

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
dfs(graph, 1, visited)