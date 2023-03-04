# https://school.programmers.co.kr/learn/courses/30/lessons/138476

def solution(k, tangerine):
    end = max(tangerine)
    
    # 크기별 귤의 개수 count
    counts = [0 for _ in range(end + 1)]
    
    for t in tangerine:
        counts[t] += 1
        
    counts.sort(reverse = True)
    acc = 0
    
    # 개수가 가장 많은 귤부터 담아 k개 이상이 되면 종료
    for i in range(len(counts)):
        acc += counts[i]
        
        if acc >= k:
            return i + 1