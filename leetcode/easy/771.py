# https://leetcode.com/problems/jewels-and-stones/

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        cnt = 0
        jewelSet = set(jewels)
        
        for j in jewelSet:
            for s in stones:
                if(j == s):
                    cnt += 1
                    
        return cnt

# set(str)도 list(str)과 같이 매개변수로 사용된 String을 형변환
# -> set이기 때문에 중복 자동 제거