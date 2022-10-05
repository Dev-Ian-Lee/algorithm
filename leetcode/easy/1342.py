# https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/description/

class Solution:
    def numberOfSteps(self, num: int) -> int:
        cnt = 0

        while(True):
            if(num == 0):
                break

            if(num % 2 == 0):
                num /= 2

            else:
                num -= 1
            
            cnt += 1

        return cnt