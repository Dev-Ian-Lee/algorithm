# https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent/description/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        self.ret = 0
        self.parents = []

        def findEvenNodes(node):
            if(not node):
                return 0

            # 값이 짝수인 노드의 자식들을 self.parents 리스트에 저장
            if(node.val % 2 == 0):
                if(node.left is not None):
                    self.parents.append(node.left)

                if(node.right is not None):
                    self.parents.append(node.right)

            findEvenNodes(node.left)
            findEvenNodes(node.right)

        def sumGrandChildren():
            # self.parents의 각 노드의 자식 값의 합 계산
            for node in self.parents:
                if(node.left is not None):
                    self.ret += node.left.val

                if(node.right is not None):
                    self.ret += node.right.val

        findEvenNodes(root)
        sumGrandChildren()

        return self.ret

