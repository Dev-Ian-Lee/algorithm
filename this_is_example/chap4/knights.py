# <이것이 취업을 위한 코딩 테스트다> 실전 문제 4-3

str = input()

x = ord(str[0]) - ord('a')
y = int(str[1]) - 1
dx = [2, 2, -2, -2, 1, 1, -1, -1]
dy = [1, -1, 1, -1, 2, -2, 2, -2]
count = 0

for i in range(8):
    nx = x + dx[i]
    ny = y + dy[i]

    if (nx >= 0 and nx <= 7) and (ny >= 0 and ny <= 7):
        count += 1

print(count)