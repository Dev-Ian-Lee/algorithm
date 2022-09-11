# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/

from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        ret = []
        max_candies = max(candies)
        
        for c in candies:
            if(c + extraCandies >= max_candies):
                ret.append(True)
                
            else:
                ret.append(False)
                
        return ret