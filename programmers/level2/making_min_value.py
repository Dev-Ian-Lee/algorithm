# https://school.programmers.co.kr/learn/courses/30/lessons/12941

def solution(A,B):
    answer = 0

    size = len(A)
    A.sort()
    B.sort(reverse = True)
    
    for i in range(size):
        answer += A[i] * B[i]
        
    return answer