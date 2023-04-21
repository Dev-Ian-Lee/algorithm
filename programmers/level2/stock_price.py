# https://school.programmers.co.kr/learn/courses/30/lessons/42584

def solution(prices):
    answer = []
    n = len(prices)
    
    for i in range(n):
        count = 0
        
        for j in range(i + 1, n):
            if prices[i] <= prices[j]:
                count += 1
                
            else:
                count = j - i
                break
                
        answer.append(count)
            
    return answer