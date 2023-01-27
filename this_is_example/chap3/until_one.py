# <이것이 취업을 위한 코딩 테스트다> 실전 문제 3-4

def sol(N, K):
    count = 0

    while (N > 1):
        if (N % K == 0):
            N /= K
            count += 1
        
        else:
            N -= 1
            count += 1

    return count

N, K = map(int, input().split())

print(sol(N, K))