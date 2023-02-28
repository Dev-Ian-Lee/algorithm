# https://school.programmers.co.kr/learn/courses/30/lessons/12939?language=python3

def solution(s):
    answer = ''
    ls = list(map(int, s.split()))
    answer = str(min(ls)) + ' ' + str(max(ls))
    
    return answer