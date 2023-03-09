# https://school.programmers.co.kr/learn/courses/30/lessons/42626

import heapq

def solution(scoville, K):
    if K == 0:
        return 0
    
    cnt = 0
    q = []
    
    # scoville리스트를 힙으로 변환(heapq.heapify()로 대체 가능)
    for s in scoville:
        heapq.heappush(q, s)
        
    while True:
        # 최소힙이기 때문에 pop()한 값은 힙 내에서 최소값
        least = heapq.heappop(q)
    
        # 최소값이 K 이상인 경우 종료
        if least >= K:
            break
            
        # 마지막으로 꺼낸 항목이 K 미만일 경우, 모든 음식을 스코빌 지수 K 이상으로 만들 수 없기 때문에 -1 반환
        if len(q) == 0:
            return -1
            
        # 두 번째로 작은 값으로 연산, 연산 횟수 증가
        cnt += 1
        second = heapq.heappop(q)
        mix = least + (second * 2)
        heapq.heappush(q, mix)
        
    return cnt       