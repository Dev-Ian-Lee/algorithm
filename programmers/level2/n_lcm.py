# https://school.programmers.co.kr/learn/courses/30/lessons/12953#

INF = int(1e9)

def solution(arr):
    for i in range(1, INF):
        cnt = 0
        
        for ele in arr:
            if i % ele == 0:
                cnt += 1
                
            if cnt == len(arr):
                return i