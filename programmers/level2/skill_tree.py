# https://school.programmers.co.kr/learn/courses/30/lessons/49993

def solution(skill, skill_trees):
    count = 0
    
    for skill_tree in skill_trees:
        order = []
        
        # 각 skill_tree 문자열에서 skill에 있는 문자를 순서대로 order 리스트에 저장
        for ch in skill_tree:
            if ch in skill:
                order.append(ch)
        
        # order리스트를 이어붙인 값과 그 길이만큼 skill을 자른 값이 같다면 가능한 스킬 트리 
        tmp = "".join(order)
        if tmp == skill[:len(tmp)]:
            count += 1
                
    return count