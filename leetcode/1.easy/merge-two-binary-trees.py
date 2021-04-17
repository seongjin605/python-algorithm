# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        tree_nodes = collections.deque( nums )
        result = collections.deque( [] )
        while len( tree_nodes ) > 0:
            node = tree_nodes.popleft()
            print('node:', node)
            if not result:
                result.append( node )
            print('result:', result)
            if node > tree_nodes.index( 0 ):
                result.append( node )
            else:
                result.appendleft( node )

        return result