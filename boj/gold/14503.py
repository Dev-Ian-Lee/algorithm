# https://www.acmicpc.net/problem/14503

import sys
import copy

# 반시계 방향 회전
def rotate(pos):
    pos -= 1

    if pos == -1:
        pos = 3

    return pos

n, m = list(map(int, sys.stdin.readline().split()))
x, y, d = list(map(int, sys.stdin.readline().split()))

room = []
for _ in range(n):
    room.append(list(map(int, sys.stdin.readline().split())))

# deepcopy로 방의 초기상태 저장
initial_room = copy.deepcopy(room)
pos = d

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

cleaned = 0
while True:
    # 현재 칸이 빈 칸(청소되지 않은 칸)인 경우 청소
    if room[x][y] == 0:
        room[x][y] = 1
        cleaned += 1

    cnt = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if room[nx][ny] == 1:
            cnt += 1

    # 주변 4칸 중 빈 칸이 없는 경우
    if cnt == 4:
        # 보고있는 방향 확인해 후진 가능할 경우 후진, 불가능할 경우 종료
        if pos == 0:
            if x + 1 <= n - 1 and initial_room[x + 1][y] != 1:
                x += 1

            else:
                break

        elif pos == 1:
            if y - 1 >= 0 and initial_room[x][y - 1] != 1:
                y -= 1

            else:
                break

        elif pos == 2:
            if x - 1 >= 0 and initial_room[x - 1][y] != 1:
                x -= 1

            else:
                break

        else:
            if y + 1 <= m - 1 and initial_room[x][y + 1] != 1:
                y += 1

            else:
                break

    # 주변 4칸 중 빈 칸이 있는 경우
    else:
        # 반시계 방향 회전
        pos = rotate(pos)

        # 보고있는 방향 확인해 빈 칸인 경우 이동
        if pos == 0:
            if x - 1 >= 0 and room[x - 1][y] == 0:
                x -= 1

        elif pos == 1:
            if y + 1 <= m - 1 and room[x][y + 1] == 0:
                y += 1

        elif pos == 2:
            if x + 1 <= n - 1 and room[x + 1][y] == 0:
                x += 1

        else:
            if y - 1 >= 0 and room[x][y - 1] == 0:
                y -= 1

print(cleaned)