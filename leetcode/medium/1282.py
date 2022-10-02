# https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/

from typing import List

class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        groups = {}
        ret = []
        
        for i in range(len(groupSizes)):
            if(groupSizes[i] in groups.keys()):
                if(len(groups[groupSizes[i]]) == groupSizes[i]):
                    ret.append(groups.pop(groupSizes[i]))
                    groups[groupSizes[i]] = [i]

                else:
                    groups[groupSizes[i]].append(i)
                    
            else:
                groups[groupSizes[i]] = [i]

        for key in groups.keys():
            ret.append(groups[key])

        # 각 항목의 길이를 기준으로 정렬
        ret.sort(key = lambda x:len(x))
        return ret
