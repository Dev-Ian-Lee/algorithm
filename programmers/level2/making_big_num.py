# https://school.programmers.co.kr/learn/courses/30/lessons/42883

def solution(number, k):
    stack = []
    
    for num in number:
        while stack and stack[-1] < num and k > 0:
            stack.pop()
            k -= 1
            
        stack.append(num)
        
    if k > 0:
        stack = stack[:-k]
    
    return ''.join(stack)