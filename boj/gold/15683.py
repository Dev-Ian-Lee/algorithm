# https://www.acmicpc.net/problem/15683

import copy

N, M = map(int, input().split())

office = []
for _ in range(N):
    office.append(list(map(int, input().split())))

# cctv 종류, 위치
cctv = []
for row in range(N):
    for col in range(M):
        if office[row][col] in [1, 2, 3, 4, 5]:
            cctv.append([office[row][col], row, col])

# 각 cctv의 가능한 방향(북: 0, 동: 1, 남: 2, 서: 3)
direction = [[],
            [[0], [1], [2], [3]],
            [[1, 3], [0, 2]],
            [[0, 1], [1, 2], [2, 3], [0, 3]],
            [[0, 1, 3], [0, 1, 2], [1, 2, 3], [0, 2, 3]],
            [[0, 1, 2, 3]]]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def observe(office, direction, x, y):
    for i in direction:
        nx = x
        ny = y
        
        # 감시할 수 있는 칸(범위가 넘어가지 않고, 벽이 아닌 칸)의 값을 -1로 변경
        while True:
            nx += dx[i]
            ny += dy[i]
            
            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                break
            
            if office[nx][ny] == 6:
                break
            
            elif office[nx][ny] == 0:
                office[nx][ny] = -1

min_value = int(1e9)

def dfs(depth, office):
    global min_value
    
    # 모든 cctv를 다 고려한 경우 종료
    if depth == len(cctv):
        count = 0
        
        # 각 행별 사각지대 개수
        for row in office:
            count += row.count(0)
            
        # 사각지대 개수의 최소값 반환
        min_value = min(min_value, count)
        return min_value
    
    tmp = copy.deepcopy(office)
    cctv_num, x, y = cctv[depth]
    
    for dir in direction[cctv_num]:
        observe(tmp, dir, x, y)
        dfs(depth + 1, tmp)
        
        # 하나의 경우의 수 고려한 뒤 배열 초기화
        tmp = copy.deepcopy(office)
        
dfs(0, office)
print(min_value)