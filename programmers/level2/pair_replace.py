# https://school.programmers.co.kr/learn/courses/30/lessons/12973

# 괄호 검사 문제와 유사하게 스택을 사용해 해결
# 문자열의 길이가 최대 1,000,000이므로, O(N)에 해결해야 한다는 것을 파악
def solution(s):
    stack = []
    
    for c in s:
        # 스택이 비어있을 경우 현재 문자 삽입
        if len(stack) == 0:
            stack.append(c)
            
        else:
            # 이전 문자와 현재 문자가 다를 경우, 현재 문자 스택에 삽입
            if stack[-1] != c:
                stack.append(c)
                
            # 같을 경우, 이전 문자 스택에서 추출
            else:
                stack.pop()

    # 스택의 길이가 0인 경우는, 모든 문자가 짝지어 제거된 것이므로 1 반환
    if len(stack) == 0:
        return 1
    
    else:
        return 0