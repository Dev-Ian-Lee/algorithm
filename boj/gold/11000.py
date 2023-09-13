# https://www.acmicpc.net/problem/11000

# 걸린 시간: -
# 시간복잡도: O(N * log N)

# 이중 for문으로 구현하니 N <= 200,000이므로 시간 초과 발생
# deque 사용, 정렬 등의 방법을 시도해도 시간 초과 발생해서 검색을 통해 해결

# 우선순위 큐(heapq) + 그리디
# 현재 강의 시작 전에 끝나는 강의가 있을 경우 강의장 대체, 없을 경우 강의장 추가

import sys
import heapq

N = int(sys.stdin.readline())
lectures = []

# N <= 200,000 이므로 입력 속도가 빠른 sys.stdin.readline() 사용
for _ in range(N):
    lectures.append(list(map(int, sys.stdin.readline().split())))
    
lectures.sort()

rooms = []
# 강의 종료 시간 저장
heapq.heappush(rooms, lectures[0][1])

for i in range(1, N):
    
    # 현재 강의 시작 전에 끝나는 강의가 있을 경우, 강의장 대체
    if rooms[0] <= lectures[i][0]:
        heapq.heappop(rooms)
        
    # 현재 강의 시작 전에 끝나는 강의가 없을 경우, 강의장 개수 증가
    heapq.heappush(rooms, lectures[i][1])
    
print(len(rooms))

# 이전 코드(시간 초과)
# ...
#
# rooms = []
# for lecture in lectures:
#     if len(rooms) == 0:
#         rooms.append(lecture[1])
#         continue
        
#     room_idx = 0
#     while True:
#         # 새로운 강의장 추가
#         if room_idx == len(rooms):
#             rooms.append(lecture[1])
#             break
        
#         # 기존 강의장의 끝나는 시간 갱신
#         if rooms[room_idx] <= lecture[0]:
#             rooms[room_idx] = lecture[1]
#             break
        
#         room_idx += 1
        
# print(len(rooms))