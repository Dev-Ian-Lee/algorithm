# <이것이 취업을 위한 코딩 테스트다> 실전 문제 8-2

# 초기 코드 : 메모이제이션을 활용하지 않아서 시간 초과 발생 가능
# X = int(input())
# memos = []
# memos.append([X])

# for _ in range(len(X)):
#     memo = memos[-1]
#     arr = []

#     for num in memo:
#         if num % 5 == 0:
#             arr.append(num // 5)

#         if num % 3 == 0:
#             arr.append(num // 3)

#         if num % 2 == 0:
#             arr.append(num // 2)

#         arr.append(num - 1)

#     memos.append(arr)

#     if 1 in arr:
#         print(len(memos) - 1)
#         break

# 개선 코드
X = int(input())

# 1 <= X <= 30000이므로 연산 횟수는 30000번 이하
dp = [0] * 30001

# 입력값이 1이면 필요한 연산 횟수는 0이므로 2부터 시작
for i in range(2, X + 1):

    # 현재의 수에서 1을 빼는 경우
    dp[i] = dp[i - 1] + 1

    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)

    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)

    if i % 5 == 0:
        dp[i] = min(dp[i], dp[i // 5] + 1)

print(dp[X])