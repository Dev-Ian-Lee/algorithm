# https://leetcode.com/problems/create-target-array-in-the-given-order/

from typing import List

class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        target = []

        for i in range(len(nums)):
            target.insert(index[i], nums[i])

        return target
