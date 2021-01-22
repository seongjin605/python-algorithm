# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List


def levelOrder(self, root: TreeNode) -> List[List[int]]:
    if root == None: return []
    treeNodes, result = [], []
    treeNodes.append(root)
    while len(treeNodes) > 0:
        current = []
        size = len(treeNodes)
        for i in range(0, size):
            node = treeNodes.pop(0)
            if node != None and node.left != None:
                treeNodes.append(node.left)
            if node != None and node.right != None:
                treeNodes.append(node.right)
            current.append(node.val)
        result.append(current)
    return result
