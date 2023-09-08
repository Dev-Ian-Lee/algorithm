# https://school.programmers.co.kr/learn/courses/30/lessons/68645?language=python3

def solution(n):
    answer = []
    triangle = [[0 for _ in range(n)] for _ in range(n)]
    x, y = -1, 0
    num = 1
    
    for i in range(n):
        for j in range(i, n):
            # 하
            if i % 3 == 0:
                x += 1
                
            # 우
            elif i % 3 == 1:
                y += 1
                
            # 상
            else:
                x -= 1
                y -= 1
                
            triangle[x][y] = num
            num += 1
            
    # 2차원 배열 triangle에서 0이 아닌 값만 answer에 추가
    for row in triangle:
        for ele in row:
            if ele != 0:
                answer.append(ele)
    
    return answer