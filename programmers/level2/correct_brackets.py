# https://school.programmers.co.kr/learn/courses/30/lessons/12909

def solution(s):
    stack = []
    
    for c in s:
        # 여는 괄호를 스택에 추가
        if c == "(":
            stack.append(c)
            
        else:
            # 닫는 괄호와 짝지어지는 여는 괄호가 스택에 없을 경우 False 반환
            if len(stack) == 0:
                return False
            
            # 스택에는 여는 괄호만 들어가기 때문에 pop()이 성공하면 짝이 맞는 것이므로 그냥 넘어감
            pre = stack.pop()
            
    # 여는 괄호의 개수가 닫는 괄호의 개수보다 많으면 False 반환
    if len(stack) != 0:
        return False

    return True