# https://school.programmers.co.kr/learn/courses/30/lessons/12924

def solution(n):
    answer = 0

    # n의 절반값 + (그 이전값 or 그 이후값) 2개의 숫자로 n을 표현할 수 있음 (ex: 15 = 7 + 8)
    # 따라서 아래와 같이 반복 횟수를 반으로 줄일 수 있음
    size = (n // 2) + 1
    
    for i in range(1, size):
        acc = 0
        
        for j in range(i, size + 1):
            acc += j

            # i부터 연속되는 수를 계속 더했을 때 n보다 커지면 스킵
            if acc > n:
                break
            
            # i부터 연속되는 수를 더했을 때 n이 되면 카운트 증가
            if acc == n:
                answer += 1
                break
    
    answer += 1
    return answer