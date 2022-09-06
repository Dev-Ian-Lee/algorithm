# https://leetcode.com/problems/running-sum-of-1d-array/

from typing import List

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        rSum: List[int] = nums
        
        for i in range(1, len(nums)):
            rSum[i] += rSum[i - 1]
            
        return rSum