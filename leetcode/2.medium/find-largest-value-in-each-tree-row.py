# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        # nodes = [root]
        nodes = collections.deque( [root] )
        result = []

        while len( nodes ) > 0:
            node_size = len( nodes )
            current = []
            for n in range( node_size ):
                node = nodes.popleft()
                if node:
                    if node.left:
                        nodes.append( node.left )
                    if node.right:
                        nodes.append( node.right )
                    current.append( node.val )
            if current:
                result.append( max( current ) )
        return result

