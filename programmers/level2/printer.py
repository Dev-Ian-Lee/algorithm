# https://school.programmers.co.kr/learn/courses/30/lessons/42587

from collections import deque

def solution(priorities, location):
    highest = max(priorities)
    
    # 문서 번호와 우선순위를 큐에 함께 저장
    queue = deque()
    for i in range(len(priorities)):
        queue.append([i, priorities[i]])
        
    seq = 1
    while True:

        # 큐 가장 앞에 있는 문서
        curr = queue[0]
        
        # 우선순위가 가장 높은 경우
        if curr[1] == highest:

            # 인쇄 요청 문서일 경우 출력된 순서 반환
            if curr[0] == location:
                return seq
            
            else:
                # 출력(추출)
                queue.popleft()
                seq += 1

                # 우선순위 갱신
                priorities.pop(priorities.index(curr[1]))
                highest = max(priorities)
                
        # 우선순위가 가장 높지 않은 경우, 큐의 맨 끝으로 이동
        else:
            tmp = queue.popleft()
            queue.append(tmp)
            
    return 0