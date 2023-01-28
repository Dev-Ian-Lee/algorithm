# <이것이 취업을 위한 코딩 테스트다> 예제 4-1

N = int(input())
moves = list(input().split())

curr = [1, 1]

for move in moves:
    if move == 'L':
        if curr[1] > 1 : 
            curr[1] -= 1

    elif move == 'R':
        if curr[1] < N:
            curr[1] += 1
    
    elif move == 'U':
        if curr[0] > 1 : 
            curr[0] -= 1
    
    elif move == 'D':
        if curr[0] < N:
            curr[0] += 1

print(curr[0], curr[1])