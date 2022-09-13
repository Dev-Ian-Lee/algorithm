# https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ret = []
        
        for i in range(len(nums)):
            cnt = 0
            for j in range(len(nums)):
                if(nums[i] > nums[j]):
                    cnt += 1
                
            ret.append(cnt)
                
        return ret