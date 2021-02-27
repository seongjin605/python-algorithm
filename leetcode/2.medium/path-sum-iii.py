# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


import collections


# https://leetcode.com/problems/path-sum-iii/
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:

        tree_nodes = collections.deque([root])
        sum = 0
        while len(tree_nodes) > 0:
            tree_size = len(tree_nodes)
            for i in range(tree_size):
                node = tree_nodes.popleft()
                print('node:', node)
                if node.left:
                    tree_nodes.append(node.left)
                if node.right:
                    tree_nodes.append(node.right)
                if node.left and node.right:
                    sum = sum + node.val
        return sum
