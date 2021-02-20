# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# https://leetcode.com/problems/insert-into-a-binary-search-tree/
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        tree_nodes = []
        tree_nodes.append( root )
        while len( tree_nodes ) > 0:
            node = tree_nodes.pop()
            print( 'node:', node )
            if node.left == None and (node.val < val):
                node = TreeNode( val )
            if node.right == None and (node.val > val):
                node = TreeNode( val )
            if node.left:
                tree_nodes.append( node.left )
            if node.right:
                tree_nodes.append( node.right )
        return root

