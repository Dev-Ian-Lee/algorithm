# https://leetcode.com/problems/strictly-palindromic-number/

class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        for i in range(2, n - 1):
            ls = []
            div = n
            
            while(True):    
                div, mod = divmod(div, i)
                ls.append(mod)
                
                if(div < 1):
                    break
                
            ls_rev = ls[::-1]
            
            if(ls_rev != ls):
                return False
            
        return True

# 모든 경우에 대해 False이기 때문에 return False 한 줄이면 구현 가능한 문제