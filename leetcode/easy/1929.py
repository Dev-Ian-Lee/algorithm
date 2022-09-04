# https://leetcode.com/problems/concatenation-of-array/

from typing import List

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans: List[int] = nums
        ans.extend(nums)
        
        return ans

# ans = nums.extend(nums)와 같이 inline으로 구현할 경우, return값 없이 nums에 nums를 이어붙임
# 즉, nums = [1, 2, 3]일 때 nums = [1, 2, 3, 1, 2, 3]이, ans = None이 됨

# ans = nums + nums도 가능