# Definition for a binary tree node.
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        tree_nodes = collections.deque([root])
        result = []
        while len(tree_nodes) > 0:
            current = collections.deque([])
            tree_size = len(tree_nodes)
            for i in range(tree_size):
                node = tree_nodes.popleft()
                if node.left:
                    tree_nodes.append(node.left)
                if node.right:
                    tree_nodes.append(node.right)
                current.append(node.val)
            result.append(current)
        return result