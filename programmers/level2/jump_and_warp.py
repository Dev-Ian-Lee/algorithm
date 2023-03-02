# https://school.programmers.co.kr/learn/courses/30/lessons/12980

def solution(n):
    cnt = 1
    
    while True:
        if n <= 1:
            break
        
        if n % 2 != 0:
            cnt += 1
            
        n = n // 2
        
    return cnt