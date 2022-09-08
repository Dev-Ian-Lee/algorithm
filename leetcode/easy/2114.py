# https://leetcode.com/problems/maximum-number-of-words-found-in-sentences/

from typing import List

class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        num_of_words = []
        
        for s in sentences:
            ls = s.split()
            num_of_words.append(len(ls))
            
        return max(num_of_words)