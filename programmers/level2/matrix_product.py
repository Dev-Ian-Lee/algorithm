# https://school.programmers.co.kr/learn/courses/30/lessons/12949

def solution(arr1, arr2):
    row = len(arr1)
    col = len(arr2[0])
    inner = len(arr2)
    
    answer = [[0 for _ in range(col)] for _ in range(row)]
    
    for i in range(row):
        for j in range(col):
            for k in range(inner):
                answer[i][j] += arr1[i][k] * arr2[k][j]
    
    return answer