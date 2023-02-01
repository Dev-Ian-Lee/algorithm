# <이것이 취업을 위한 코딩 테스트다> 실전 문제 6-9

N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort(reverse = True)

for i in range(K):
    if A[i] < B[i]:
        A[i], B[i] = B[i], A[i]
    
    else:
        break

print(sum(A))