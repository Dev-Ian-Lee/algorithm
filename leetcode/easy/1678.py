# https://leetcode.com/problems/goal-parser-interpretation/

class Solution:
    def interpret(self, command: str) -> str:
        ret = command
        ret = ret.replace("()", "o")
        ret = ret.replace("(al)", "al")

        return ret