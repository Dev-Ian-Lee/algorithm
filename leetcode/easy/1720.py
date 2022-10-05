# https://leetcode.com/problems/decode-xored-array/

from typing import List

class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        arr = [first]
        
        for i in range(len(encoded)):
            arr.append(encoded[i] ^ arr[i])
            
        return arr

# XOR 연산은 두 비트의 값이 다르면 1, 같으면 0
# 즉, 같은 10진수끼리의 XOR 연산 결과는 0이 됨
# 문제에서 아래와 같은 식이 주어짐
# encoded[i] = arr[i] ^ arr[i + 1]
# -> encoded[i] ^ encoded[i] ^ arr[i + 1] = arr[i] ^ arr[i + 1] ^ encoded[i] ^ arr[i + 1]
# -> arr[i + 1] = arr[i] ^ encoded[i]