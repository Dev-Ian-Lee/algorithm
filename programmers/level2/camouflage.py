# https://school.programmers.co.kr/learn/courses/30/lessons/42578

def solution(clothes):
    dic = {}
    categories = set()
    
    # 딕셔너리에 옷의 카테고리별 리스트 저장
    for c in clothes:
        name = c[0]
        category = c[1]
        categories.add(category)
        
        if category in dic.keys():
            dic[category].append(name)
            
        else:
            dic[category] = [name]

    # 가능한 조합의 수 계산
    # 상의가 2개(A, B), 하의가 2개(C, D)일 경우
    # 상의 경우의 수 : A 입기, B 입기, 둘 다 안 입기 -> 3
    # 하의 경우의 수 : C 입기, D 입기, 둘 다 안 입기 -> 3
    mul = 1
    for c in categories:
        mul *= len(dic[c]) + 1
        
    # 아무것도 입지 않은 경우 차감해 반환
    return mul - 1