# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def helper(left, right):
            if right < left:
                return None
            mid = left + (right - left) // 2
            node = TreeNode(nums[mid])
            node.left = helper(left, mid - 1)
            node.right = helper(mid + 1, right)
            return node
        return helper(0, len(nums) - 1)