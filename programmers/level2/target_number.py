# https://school.programmers.co.kr/learn/courses/30/lessons/43165

from collections import deque

def solution(numbers, target):
    q = deque()
    q.append(numbers[0])
    q.append(numbers[0] * (-1))
    
    idx = 1
    while q:
        if idx == len(numbers):
            break
        
        # 매 반복마다 연산 횟수가 2배씩 증가
        for _ in range(2 ** idx):

            # 큐에서 이전 항 꺼낸 뒤 현재 항을 더한 값, 뺀 값을 각각 큐에 더해줌
            popped = q.popleft()

            q.append(popped + numbers[idx])
            q.append(popped - numbers[idx])
        
        idx += 1
        
    return q.count(target)