# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        tree_nodes = collections.deque([root])
        result = []
        while len(tree_nodes) > 0:
            node_size = len(tree_nodes)
            for i in range(0, node_size):
                node = tree_nodes.popleft()
                if node:
                    if node.left:
                        tree_nodes.append(node.left)
                    if node.right:
                        tree_nodes.append(node.right)
                        result.append(node.val)
        return result