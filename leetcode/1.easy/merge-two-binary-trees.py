# https://leetcode.com/problems/merge-two-binary-trees/
# Definition for a binary tree node.
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        first, second = collections.deque( [root1] ), collections.deque( [root2] )
        result = []

        while len( first ) > 0 and len( second ) > 0:
            first_pop = first.popleft()
            second_pop = second.popleft()

            value = first_pop.val + second_pop.val

            if first_pop.left:
                first.append( first_pop.left )
            if first_pop.right:
                first.append( first_pop.right )
            if second_pop.left:
                first.append( second_pop.left )
            if second_pop.right:
                first.append( second_pop.right )

            result.append( value )

        return result