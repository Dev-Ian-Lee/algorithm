# https://school.programmers.co.kr/learn/courses/30/lessons/118667

# 걸린 시간: -
# 시간복잡도: ???

# 합이 더 큰 큐(덱)에서 더 작은 큐로 원소를 옮김
# 시간 초과, 일부 케이스 틀리는 걸 해결 못해서 검색
# while문 내에서 sum을 계산을 반복하는 것 대신 밖에서 계산한 뒤 증감 -> 이것만으로도 대부분의 시간 초과 케이스 해결
# (큐 길이 * 4)회 이상 반복했을 경우 종료하는 조건을 떠올리지 못함

from collections import deque

def solution(queue1, queue2):
    if len(queue1) == 1 and queue1[0] != queue2[0]:
        return -1
    
    answer = 0
    
    q1 = deque(queue1)
    q2 = deque(queue2)
    
    # sum을 while문 외부에서 계산하는 것이 효율적
    sum_q1 = sum(q1)
    sum_q2 = sum(q2)
    
    # 두 큐의 총 합이 2로 나눠떨어지지 않을 경우 -1 반환
    if (sum_q1 + sum_q2) % 2 != 0:
        return -1
    
    cnt = 0
    while True:
        # 큐 길이의 4배만큼 반복 후에도 반으로 나눌 수 없는 경우 -1 반환
        if answer == 4 * len(queue1):
            return -1
        
        if sum_q1 == sum_q2:
            return answer
        
        # 두 큐 중 합이 더 큰 곳에서 작은 곳으로 원소 이동
        elif sum_q1 > sum_q2:
            popped = q1.popleft()
            q2.append(popped)
            sum_q1 -= popped
            sum_q2 += popped
            
        else:
            popped = q2.popleft()
            q1.append(popped)
            sum_q2 -= popped
            sum_q1 += popped
            
        # 작업 횟수 증가
        answer += 1
    
# 이전 코드(시간 초과, 틀림)
# from collections import deque

# def solution(queue1, queue2):
#     if len(queue1) == 1 and queue1[0] != queue2[0]:
#         return -1
    
#     answer = int(1e9)
#     q1 = deque(queue1)
#     q2 = deque(queue2)
    
#     cnt = 0
#     while True:
#         sum_q1 = sum(q1)
#         sum_q2 = sum(q2)
        
#         if sum_q1 == sum_q2:
#             if 0 < cnt < answer:
#                 answer = cnt
                
#             break
            
#         if len(q1) == 0 or len(q2) == 0:
#             break
        
#         elif sum_q1 > sum_q2:
#             popped = q1.popleft()
#             q2.append(popped)
#             cnt += 1
            
#         else:
#             popped = q2.popleft()
#             q1.append(popped)
#             cnt += 1
    
#     if answer == int(1e9):
#         return -1
    
#     else:
#         return answer