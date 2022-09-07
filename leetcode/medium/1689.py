# https://leetcode.com/problems/partitioning-into-minimum-number-of-deci-binary-numbers/

class Solution:
    def minPartitions(self, n: str) -> int:
        nums = list(n)

        return max(nums)

# n = 82734일 때,
# 각 자리 중 최대값은 8
# -> 각 자리의 값이 0인 5자리 deci-binary값을 8개 준비

# 8 2 7 3 4
# 0 0 0 0 0
# 0 0 0 0 0
# 0 0 0 0 0
# 0 0 0 0 0
# 0 0 0 0 0
# 0 0 0 0 0
# 0 0 0 0 0
# 0 0 0 0 0

# 맨 앞 자리인 8을 만들려면 모든 deci-binary의 맨 앞 자리가 1이 되어야 함
# 나머지 자리는 8보다 작기 때문에 순서 상관없이 개수만 맞도록 0을 1로 대체
# 즉, 각 자리 중 최대값이 답(필요한 deci-binary의 개수)