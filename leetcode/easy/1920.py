# https://leetcode.com/problems/build-array-from-permutation/
# Permutation : 순열

from typing import List


class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans: List[int] = [0] * len(nums)

        for i in range(len(nums)):
            ans[i] = nums[nums[i]]

        return ans

# typing 모듈은 파이썬에서도 타입을 지정하는 것같은 효과