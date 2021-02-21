# Definition for a binary tree node.
import collections
from typing import List

# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []

        tree_nodes = collections.deque( [root] )
        result = []
        check = False  # False 왼쪽부터 뺌, True: 오른쪽부터 뺌

        while len( tree_nodes ) > 0:
            # current = []
            current = collections.deque( [] )
            tree_size = len( tree_nodes )
            for i in range( tree_size ):
                node = None
                node = tree_nodes.popleft()

                if check == True:
                    # current.insert(0, node.val)
                    current.appendleft( node.val )
                else:
                    current.append( node.val )
                    # current.append(node.val)

                if node.left:
                    tree_nodes.append( node.left )
                if node.right:
                    tree_nodes.append( node.right )
            result.append( current )
            check = not check

        return result

