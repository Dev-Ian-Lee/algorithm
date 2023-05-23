# https://school.programmers.co.kr/learn/courses/30/lessons/12913

def solution(land):
    for i in range(1, len(land)):
        for j in range(4):
            # 현재 항에 이전 항에서 j열을 제외한 최대값 더함
            land[i][j] += max(land[i - 1][:j] + land[i - 1][j + 1:])
    
    return max(land[-1])