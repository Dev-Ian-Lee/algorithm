# https://www.acmicpc.net/problem/10703

import sys

r, s = list(map(int, sys.stdin.readline().split()))
picture = [sys.stdin.readline() for _ in range(r)]

move = int(1e9)
for x in range(s):
    lowest_meteor = -1
    highest_ground = int(1e9)
    flag = False

    for y in range(r):
        if picture[y][x] == 'X':
            lowest_meteor = max(lowest_meteor, y)

            # 유성의 유무 확인
            flag = True
            
        elif picture[y][x] == '#':
            highest_ground = min(highest_ground, y)

    # 유성이 있는 열에서 유성의 높이와 땅의 높이 차의 최솟값
    if flag:
        move = min(abs(lowest_meteor - highest_ground) - 1, move)

new_picture = [["."] * s for _ in range(r)]
for x in range(r):
    for y in range(s):
        # 유성은 move만큼 밑으로 움직이고, 땅은 그대로
        if picture[x][y] == "X":
            new_picture[x + move][y] = "X"

        elif picture[x][y] == "#":
            new_picture[x][y] = "#"

for line in new_picture:
    for c in line:
        sys.stdout.write(c)

    sys.stdout.write("\n")