# https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        s = str(n)
        ls = list(s)
        ls = list(map(int, ls))
        
        product_n = 1
        sum_n = 0
        
        for ele in ls:
            product_n *= ele
            sum_n += ele
            
        return product_n - sum_n