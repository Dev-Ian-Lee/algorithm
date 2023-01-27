# <이것이 취업을 위한 코딩 테스트다> 실전 문제 3 - 2

# 초기 코드
# def sol(nums, M, K):
#     nums.sort(reverse = True)
#     ans = 0

#     for i in range(1, M + 1):
#         if (i % (K + 1) == 0 and i != 0):
#             ans += nums[1]
        
#         else:
#             ans += nums[0]

#     return ans

# N, M, K = map(int, input().split())
# nums = list(map(int, input().split()))

# print(sol(nums, M, K))

# 개선 코드 : 반복문이 없기 때문에 M이 100억 이상이어도 시간 초과 X
def sol(nums, M, K):
    nums.sort()
    largest = nums[-1]
    second_largest = nums[-2]

    repeat_count = M // (K + 1)

    ans = 0
    ans += largest * (repeat_count * K + (M % (K + 1)))
    ans += second_largest * repeat_count

    return ans

N, M, K = map(int, input().split())
nums = list(map(int, input().split()))

print(sol(nums, M, K))