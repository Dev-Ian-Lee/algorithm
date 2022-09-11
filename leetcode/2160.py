# https://leetcode.com/problems/minimum-sum-of-four-digit-number-after-splitting-digits/
# 가장 작은 두 숫자를 찾아서 10의 자리로, 나머지 두 숫자는 1의 자리로 사용

class Solution:
    def minimumSum(self, num: int) -> int:
        num_str = str(num)
        nums = list(num_str)

        nums = list(map(int, nums))
        nums.sort()

        ret = (nums[0] + nums[1]) * 10 + nums[2] + nums[3]
        return ret

# map(int(), nums) X
# map(int, nums) O