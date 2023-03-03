# https://school.programmers.co.kr/learn/courses/30/lessons/42747

def solution(citations):
    h_index = 0
    n = len(citations)
    
    citations.sort()
    
    for i in range(n):
        if len(citations[i:]) <= citations[i]:
            if len(citations[i:]) > h_index:
                h_index = len(citations[i:])
    
    return h_index