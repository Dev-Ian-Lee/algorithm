# https://leetcode.com/problems/final-value-of-variable-after-performing-operations/

from typing import List

class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x = 0
        
        for op in operations:
            if(op in ["--X", "X--"]):
                x -= 1
                
            elif(op in ["++X", "X++"]):
                x += 1
                
        return x


        
        # for op in operations:
        #     if("-" in op):
        #         x -= 1
                
        #     elif("+" in op):
        #         x += 1
                
        # return x        