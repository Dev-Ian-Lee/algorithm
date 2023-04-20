# https://school.programmers.co.kr/learn/courses/30/lessons/43164

def solution(tickets):
    route = {}
    
    for t in tickets:
        if t[0] in route:
            route[t[0]].append(t[1])
            
        else:
            route[t[0]] = [t[1]]
            
    for key in route:
        route[key].sort(reverse = True)
        
    stack = ["ICN"]
    visited = []
    
    while len(stack) > 0:
        top = stack[-1]
        
        if top not in route or len(route[top]) == 0:
            visited.append(stack.pop())
            
        else:
            stack.append(route[top].pop())
            
    return visited[::-1]