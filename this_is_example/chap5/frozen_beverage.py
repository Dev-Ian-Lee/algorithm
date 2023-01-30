# <이것이 취업을 위한 코딩 테스트다> 실전 문제 5-7

N, M = map(int, input().split())

graph = []
for _ in range(N):
    # 공백 없는 문자열을 리스트로 변환 시 split() 사용 X
    graph.append(list(map(int, input())))

def dfs(x, y):
    if x <= -1 or x >= N or y <= -1 or y >= M:
        return False
    
    if graph[x][y] == 0:
        graph[x][y] = 1

        # 해당 위치의 상하좌우 재귀적으로 방문
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)

        return True

    return False

result = 0

# 모든 노드에 대해 반복
for i in range(N):
    for j in range(M):
        # True가 반환된 횟수 == 생성될 아이스크림 개수
        if dfs(i, j) == True:
            result += 1

print(result)