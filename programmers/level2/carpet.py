# https://school.programmers.co.kr/learn/courses/30/lessons/42842#

def solution(brown, yellow):
    n = brown + yellow
    
    for i in range(1, n + 1):
        if n % i == 0:
            num = n // i
            
            # i는 가로, num은 세로에 해당하므로 위아래 1칸씩 총 2칸씩을 뺀 값의 곱이 노란 칸의 개수와 같아야 함
            if i >= num and (i - 2) * (num - 2) == yellow:
                return [i, num]