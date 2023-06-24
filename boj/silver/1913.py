# https://www.acmicpc.net/problem/1913

import sys

n = int(sys.stdin.readline())
target = int(sys.stdin.readline())

matrix = [[0 for _ in range(n)] for _ in range(n)]

rotation = 0
num = n ** 2
curr = [0, 0]
target_location = []

# 찾으려는 수가 n^2인 경우
if target == num:
    target_location = [1, 1]

while True:
    # 모든 수를 저장했을 경우 종료
    if num == 0:
        break

    matrix[curr[0]][curr[1]] = num

    # 하
    if rotation == 0:
        if curr[0] + 1 >= n or matrix[curr[0] + 1][curr[1]] != 0:
            rotation += 1

        else:
            curr[0] += 1
            num -= 1

    # 우
    elif rotation == 1:
        if curr[1] + 1 >= n or matrix[curr[0]][curr[1] + 1] != 0:
            rotation += 1

        else:
            curr[1] += 1
            num -= 1

    # 상
    elif rotation == 2:
        if curr[0] - 1 < 0 or matrix[curr[0] - 1][curr[1]] != 0:
            rotation += 1

        else:
            curr[0] -= 1
            num -= 1

    # 좌
    elif rotation == 3:
        if curr[1] - 1 < 0 or matrix[curr[0]][curr[1] - 1] != 0:
            rotation = 0

            # 정중앙에 1 저장
            if num == 1:
                matrix[curr[0]][curr[1]] = num
                num -= 1

        else:
            curr[1] -= 1
            num -= 1

    # 찾으려는 수의 좌표 저장
    if target == num:
        target_location = [curr[0] + 1, curr[1] + 1]

for mat in matrix:
    for m in mat:
        print(m, end = " ")

    print()

print(target_location[0], target_location[1])