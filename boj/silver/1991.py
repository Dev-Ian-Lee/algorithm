# https://www.acmicpc.net/problem/1991

# 걸린 시간: -
# 시간복잡도: O(N)

# 노드 클래스는 구현했는데 노드를 엮어서 트리로 구현하는 방법이 생각이 안 나서 검색해서 해결
# 결과적으로 모든 노드를 다 방문해야 하기 때문에 시간복잡도는 O(N)

import sys

class Node:
    def __init__(self, value):
        self.value = value
        self.left = ""
        self.right = ""

# 전위 순회
# 노드(루트)를 매개변수로 받아서, 왼쪽 노드가 있으면 왼쪽을, 오른쪽 노드가 있으면 오른쪽을 탐색
def preorder(node):
    print(node.value, end = "")
    
    if node.left:
        preorder(tree[node.left])
    
    if node.right:
        preorder(tree[node.right])
    
# 중위 순회
def inorder(node):
    if node.left:
        inorder(tree[node.left])
        
    print(node.value, end = "")
    
    if node.right:
        inorder(tree[node.right])
    
# 후위 순회
def postorder(node):
    if node.left:
        postorder(tree[node.left])
    
    if node.right:
        postorder(tree[node.right])
        
    print(node.value, end = "")

# 딕셔너리 형태로 트리 구현
tree = {}
        
N = int(sys.stdin.readline())
for _ in range(N):
    val, l, r = sys.stdin.readline().split()
    node = Node(val)
    
    # 자식 노드가 있는 경우에만 연결
    if l != ".":
        node.left = l
        
    if r != ".":
        node.right = r

    # {"A": Node(A, B, C), "B": Node(B, D, ""), ...}
    tree[val] = node

preorder(tree["A"])
print()
inorder(tree["A"])
print()
postorder(tree["A"])