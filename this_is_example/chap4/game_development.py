# <이것이 취업을 위한 코딩 테스트다> 실전 문제 4-4

# 초기 코드
# N, M = map(int, input().split())
# curr_row, curr_col, sight = map(int, input().split())
# game_map = []

# for _ in range(N):
#     game_map.append(list(map(int, input().split())))

# game_map[curr_row][curr_col] = 1
# visit_count = 1

# while(True):
#     if sight == 0:
#         if curr_col - 1 >= 0 and game_map[curr_row][curr_col - 1] == 0:
#             game_map[curr_row][curr_col - 1] = 1
#             curr_col -= 1
#             visit_count += 1
#             sight = 1

#         elif curr_row + 1 < N and game_map[curr_row + 1][curr_col] == 0:
#             game_map[curr_row + 1][curr_col] = 1
#             curr_row += 1
#             visit_count += 1
#             sight = 2
            
#         elif curr_col + 1 < M and game_map[curr_row][curr_col + 1] == 0:
#             game_map[curr_row][curr_col + 1] = 1
#             curr_col += 1
#             visit_count += 1
#             sight = 3

#         elif curr_row - 1 >= 0 and game_map[curr_row - 1][curr_col] == 0:
#             game_map[curr_row - 1][curr_col] = 1
#             curr_row -= 1
#             visit_count += 1
#             sight = 0

#         else:
#             curr_row += 1

#             if game_map[curr_row][curr_col] == 1:
#                 break

#     elif sight == 1:
#         if curr_row + 1 < N and game_map[curr_row + 1][curr_col] == 0:
#             game_map[curr_row + 1][curr_col] = 1
#             curr_row += 1
#             visit_count += 1
#             sight = 2

#         elif curr_col + 1 < M and game_map[curr_row][curr_col + 1] == 0:
#             game_map[curr_row][curr_col + 1] = 1
#             curr_col += 1
#             visit_count += 1
#             sight = 3

#         elif curr_row - 1 >= 0 and game_map[curr_row - 1][curr_col] == 0:
#             game_map[curr_row - 1][curr_col] = 1
#             curr_row -= 1
#             visit_count += 1
#             sight = 0

#         elif curr_col - 1 >= 0 and game_map[curr_row][curr_col - 1] == 0:
#             game_map[curr_row][curr_col - 1] = 1
#             curr_col -= 1
#             visit_count += 1
#             sight = 1

#         else:
#             curr_col += 1

#             if game_map[curr_row][curr_col] == 1:
#                 break

#     elif sight == 2:
#         if curr_col + 1 < M and game_map[curr_row][curr_col + 1] == 0:
#             game_map[curr_row][curr_col + 1] = 1
#             curr_col += 1
#             visit_count += 1
#             sight = 3

#         elif curr_row - 1 >= 0 and game_map[curr_row - 1][curr_col] == 0:
#             game_map[curr_row - 1][curr_col] = 1
#             curr_row -= 1
#             visit_count += 1
#             sight = 0

#         elif curr_col - 1 >= 0 and game_map[curr_row][curr_col - 1] == 0:
#             game_map[curr_row][curr_col - 1] = 1
#             curr_col -= 1
#             visit_count += 1
#             sight = 1

#         elif curr_row + 1 < N and game_map[curr_row + 1][curr_col] == 0:
#             game_map[curr_row + 1][curr_col] = 1
#             curr_row += 1
#             visit_count += 1
#             sight = 2

#         else:
#             curr_row -= 1

#             if game_map[curr_row][curr_col] == 1:
#                 break

#     elif sight == 3:
#         if curr_row - 1 >= 0 and game_map[curr_row - 1][curr_col] == 0:
#             game_map[curr_row - 1][curr_col] = 1
#             curr_row -= 1
#             visit_count += 1
#             sight = 0

#         elif curr_col - 1 >= 0 and game_map[curr_row][curr_col - 1] == 0:
#             game_map[curr_row][curr_col - 1] = 1
#             curr_col -= 1
#             visit_count += 1
#             sight = 1

#         elif curr_row + 1 < N and game_map[curr_row + 1][curr_col] == 0:
#             game_map[curr_row + 1][curr_col] = 1
#             curr_row += 1
#             visit_count += 1
#             sight = 2

#         elif curr_col + 1 < M and game_map[curr_row][curr_col + 1] == 0:
#             game_map[curr_row][curr_col + 1] = 1
#             curr_col += 1
#             visit_count += 1
#             sight = 3

#         else:
#             curr_col -= 1

#             if game_map[curr_row][curr_col] == 1:
#                 break

# print(visit_count)

# 개선 코드
N, M = map(int, input().split())

x, y, sight = map(int, input().split())
game_map = []

# 방문한 위치를 저장하기 위한 map
visited_map = [[0] * M for _ in range(N)]

for _ in range(N):
    game_map.append(list(map(int, input().split())))

visited_map[x][y] = 1
visit_count = 1

# 반시계 방향으로 회전 시 이동할 좌표
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def turn_left():
    global sight
    sight -= 1

    if sight == -1:
        sight = 3

turn_count = 0

while True:
    turn_left()

    nx = x + dx[sight]
    ny = y + dy[sight]

    if visited_map[nx][ny] == 0 and game_map[nx][ny] == 0:
        visited_map[nx][ny] = 1
        x = nx
        y = ny
        visit_count += 1
        turn_count = 0
        continue

    else:
        turn_count += 1

    if turn_count == 4:
        nx = x - dx[sight]
        ny = y - dy[sight]

        if game_map[nx][ny] == 0:
            x = nx
            y = ny
            turn_count = 0
        
        else:
            break

print(visit_count)