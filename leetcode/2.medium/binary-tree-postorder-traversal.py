# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List

# https://leetcode.com/problems/binary-tree-postorder-traversal/submissions/
class Solution:
    '''
    preorder:  root-left-right
    inorder:   left-root-right
    postorder: left-right-rooot
    '''

    def postorderTraversal(self, root: TreeNode) -> List[int]:
        treeNodes, output = [], []
        treeNodes.append( root )

        while len( treeNodes ) > 0:
            node = treeNodes.pop()
            if node != None:
                output.append( node.val )
            else:
                break;
            if node.left != None:
                treeNodes.append( node.left )
            if node.right != None:
                treeNodes.append( node.right )

        return output[::-1]
