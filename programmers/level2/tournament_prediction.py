# https://school.programmers.co.kr/learn/courses/30/lessons/12985

def solution(n,a,b):
    cnt = 1
    ls = []
    
    for i in range(1, n, 2):
        ls.append([i, i + 1])

    while True:
        for ele in ls:
            if (a in ele) and (b in ele):
                return cnt
            
        cnt += 1
        curr = []
        
        for idx in range(0, len(ls) - 1, 2):
            curr.append(ls[idx] + ls[idx + 1])
        
        ls = curr[0:]