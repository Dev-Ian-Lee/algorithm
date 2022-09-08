# https://leetcode.com/problems/richest-customer-wealth/

from typing import List

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        M = 0
        
        for acc in accounts:
            wealth = sum(acc)
            
            if(wealth > M):
                M = wealth
                
        return M


# return max(map(sum, accounts))