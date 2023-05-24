# https://school.programmers.co.kr/learn/courses/30/lessons/42583

from collections import deque

def solution(bridge_length, weight, truck_weights):
    trucks = deque(truck_weights[:])
    crossing = deque()
    time_spent = deque()
    
    curr_weight = 0
    elapsed_time = 0
    
    while True:
        # 모든 트럭이 다리를 지난 경우 종료
        if len(trucks) == 0 and len(crossing) == 0:
            break
        
        # 맨 앞의 트럭이 다리를 다 건넌 경우
        if len(time_spent) > 0:
            if time_spent[0] == bridge_length:
                popped = crossing.popleft()
                curr_weight -= popped
                time_spent.popleft()
        
        # 다음 트럭이 다리에 올라갈 수 있는 경우
        if len(trucks) != 0:
            if curr_weight + trucks[0] <= weight:
                truck = trucks.popleft()

                crossing.append(truck)
                curr_weight += truck
                time_spent.append(0)
        
        # 전체 트럭의 시간 1씩 증가
        for i in range(len(time_spent)):
            time_spent[i] += 1
            
        elapsed_time += 1
        
    return elapsed_time