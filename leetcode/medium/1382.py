# https://leetcode.com/problems/balance-a-binary-search-tree/description/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 시간복잡도 : O(n)
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        nodes = []

        # in-order로 BST 탐색 -> 노드의 값 오름차순 정렬
        def inOrderTraverse(node):
            if(not node):
                return

            inOrderTraverse(node.left)
            nodes.append(node)
            inOrderTraverse(node.right)

        def makeBalancedBST(start, end):
            if(start > end):
                return None

            mid = (start + end) // 2

            # 리스트의 중앙값은 root, 그 이전은 왼쪽 자식, 그 이후는 오른쪽 자식
            root = nodes[mid]
            root.left = makeBalancedBST(start, mid - 1)
            root.right = makeBalancedBST(mid + 1, end)

            return root

        inOrderTraverse(root)
        return makeBalancedBST(0, len(nodes) - 1)