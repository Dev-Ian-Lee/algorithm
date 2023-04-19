# https://school.programmers.co.kr/learn/courses/30/lessons/42746

def solution(numbers):
    answer = ''
    converted = []
    
    for num in numbers:
        converted.append(str(num))
    
    # 첫 자리가 같은 경우, 원소가 1000 이하이므로 해당 원소를 이어붙인 것의 앞 4자리가 클수록 우선순위 높음
    converted.sort(key = lambda x : (x * 4)[:4], reverse = True)
    
    # 모두 0으로 이루어진 수는 '0000' 같이 0 여러 개가 아닌 '0' 하나만 return
    if converted[0] == '0':
        answer = '0'
    
    else:
        for s in converted:
            answer += s
    
    return answer