# https://school.programmers.co.kr/learn/courses/30/lessons/87390

def solution(n, left, right):
    arr = []
    
    for num in range(left, right + 1):
        arr.append(max(num // n, num % n) + 1)
        
    return arr