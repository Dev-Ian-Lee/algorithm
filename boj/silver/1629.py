# https://www.acmicpc.net/problem/1629

# 걸린 시간: -
# 시간복잡도: O(log B)

# A를 실제로 B번 거듭제곱하면 시간 초과가 발생하기 때문에 수학 개념과 분할정복을 활용해 해결하는 문제
# 2^32의 경우, 실제로 32번 곱하는 것보다 (2^16)^2로 17번 곱하는 것이 빠르고, 이를 계속 절반씩 줄여나가면 총 7번만에 계산 가능

A, B, C = map(int, input().split())
    
def recursion(A, B, C):
    if B == 1:
        return A % C
    
    # B가 짝수일 경우, A의 (B // 2) 승을 구한 뒤 제곱
    if B % 2 == 0:
        return (recursion(A, B // 2, C) ** 2) % C
    
    # 홀수일 경우, 1승 추가
    else:
        return ((recursion(A, B // 2, C) ** 2) * A) % C

print(recursion(A, B, C))