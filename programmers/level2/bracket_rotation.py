# https://school.programmers.co.kr/learn/courses/30/lessons/76502

def solution(s):
    cnt = 0
    initial_s = s[:]
    
    # 회전하지 않은 초기 문자열의 괄호가 올바른지 검사
    if check_brackets(s) == True:
        cnt += 1
        
    # 괄호 회전
    first = s[0]
    s = s[1:] + first
    
    while True:
        # 초기 문자열과 같아지면 break
        if s == initial_s:
            break
        
        if check_brackets(s) == True:
            cnt += 1
            
        first = s[0]
        s = s[1:] + first
        
    return cnt

# 올바른 괄호일 경우 True를, 아닐 경우 False 반환            
def check_brackets(s):
    stack = []
    
    for c in s:
        if c in '({[':
            stack.append(c)
            
        else:
            if len(stack) == 0:
                return False
            
            popped = stack.pop()
            
            if c == ')' and popped != '(':
                return False
            
            elif c == '}' and popped != '{':
                return False
            
            elif c == ']' and popped != '[':
                return False
    
    if len(stack) == 0:
        return True