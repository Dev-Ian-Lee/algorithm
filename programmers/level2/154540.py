# https://school.programmers.co.kr/learn/courses/30/lessons/154540

# 걸린 시간: 50min
# 시간복잡도: O(N^4)

# 완전 탐색 + bfs
# 배열의 최대 크기가 100 * 100 이기 때문에 시간 초과 발생 X
# 테스트 21, 23 실패 -> 시작 노드를 방문 확인, 처리해야함을 주의

from collections import deque

visited = []

def solution(maps):
    global visited
    
    answer = []
    
    row = len(maps)
    col = len(maps[0])
    visited = [[0 for _ in range(col)] for _ in range(row)]
    
    for i in range(row):
        for j in range(col):
            tmp = bfs(i, j, maps, row, col)
            
            if tmp != 0:
                answer.append(tmp)
            
    # 지낼 수 있는 무인도가 없는 경우
    if len(answer) == 0:
        return [-1]
    
    answer.sort()
    return answer
            
    
def bfs(i, j, maps, row, col):
    q = deque()
    total = 0
    
    if maps[i][j] == "X":
        return 0
    
    # 시작 노드 방문 확인 및 처리
    else:
        if visited[i][j] == 0:
            q.append([i, j])
            visited[i][j] = 1
            total = int(maps[i][j])
    
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]
    
    # 무인도별 값의 총합 반환
    while q:
        x, y = q.pop()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if (0 <= nx < row and 0 <= ny < col) and maps[nx][ny] != "X" and visited[nx][ny] == 0:
                q.append([nx, ny])
                visited[nx][ny] = 1
                
                total += int(maps[nx][ny])
                
    return total