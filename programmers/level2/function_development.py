# https://school.programmers.co.kr/learn/courses/30/lessons/42586

def solution(progresses, speeds):
    size = len(progresses)
    days_left = []
    
    # 각 기능의 남은 일 수 계산
    for i in range(size):
        for j in range(1, 101):
            if progresses[i] + speeds[i] * j >= 100:
                days_left.append(j)
                break
    
    answer = []
    
    # 각 날짜마다 배포할 기능의 개수 계산
    i = 0
    while True:

        # 마지막 기능이 배포되지 않은 경우
        if i == size - 1:
            answer.append(1)
            break
        
        # 마지막 기능이 이전 기능과 함께 배포된 경우, 그냥 break
        if i == size:
            break
        
        cnt = 1
        
        for j in range(i + 1, size):

            # 다음 기능이 이미 완성되었다면 현재 기능과 함께 배포
            if days_left[j] <= days_left[i]:
                cnt += 1
                
                if j == size - 1:
                    i = size
                    break
            
            # 완성되지 않은 기능부터 반복
            else:
                i = j
                break
                
        answer.append(cnt)
    
    return answer