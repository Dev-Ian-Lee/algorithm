# https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

from typing import List

# class Solution:
#     def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
#         ret = []
        
#         for i in range(len(nums)):
#             cnt = 0
#             for j in range(len(nums)):
#                 if(nums[i] > nums[j]):
#                     cnt += 1
                
#             ret.append(cnt)
                
#         return ret

# 코드 개선, 시간복잡도는 그대로(O(n^2))
# list index() 메소드의 시간복잡도가 O(n)이기 때문
# class Solution:
#     def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
#         sorted_nums = sorted(nums)
#         ret = []
        
#         for num in nums:
#             ret.append(sorted_nums.index(num))
                
#         return ret

# 시간복잡도 개선(O(n^2) -> O(nlogn))
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)
        indexes = {}
        ret = []
        
        for i in range(len(nums)):
            # 해당 항목보다 작은 개수를 세기 위해, 처음 나오는 인덱스만 사용(갱신 X)
            if(sorted_nums[i] not in indexes.keys()):
                indexes[sorted_nums[i]] = i

        for i in range(len(nums)):
            ret.append(indexes[nums[i]])
                
        return ret