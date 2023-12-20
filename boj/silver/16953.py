# https://www.acmicpc.net/problem/16953

# 걸린 시간: 20min
# 시간복잡도: O(log N)

def solution():
    A, B = map(int,input().split())

    r = 1
    while(B != A):
        r += 1
        tmp = B
        
        if B % 10 == 1:
            B //= 10
            
        elif B % 2 == 0:
            B //= 2
        
        if tmp == B:
            return -1
    else:
        return r
    
print(solution())