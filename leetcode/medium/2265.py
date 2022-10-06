# https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/description/

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        self.num = 0
        self.node_cnt = 0
        self.ret = 0

        def sum_subtree(node):
            if(not node):
                return 0

            # 노드값의 합과 노드의 개수 증가
            self.num += node.val
            self.node_cnt += 1

            sum_subtree(node.left)
            sum_subtree(node.right)

        def avg_subtree(node):
            # 리프노드 탐색 이후 종료
            if(not node):
                return 0

            # 각 노드가 속한 서브트리의 값의 합 계산
            sum_subtree(node)

            # 서브트리의 평균과 해당 노드의 값이 같으면 카운트 증가
            if(node.val == self.num // self.node_cnt):
                self.ret += 1

            # 다음 노드를 탐색하기 위해 값의 합(num), 노드의 개수(node_cnt) 초기화
            self.num = 0
            self.node_cnt = 0

            avg_subtree(node.left)
            avg_subtree(node.right)

        avg_subtree(root)
        return self.ret
            

