# https://school.programmers.co.kr/learn/courses/30/lessons/131701

def solution(elements):
    size = len(elements)
    elements += elements
    combinations = set()
    
    for i in range(size):
        combinations.add(elements[i])
        
        acc = elements[i]
        for j in range(i + 1, i + size):
            acc += elements[j]
            combinations.add(acc)
    
    return len(combinations)