# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# https://leetcode.com/problems/palindrome-linked-list/submissions/
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head: return True

        nodes = []
        nodes.append( head )

        result = []
        while len( nodes ) > 0:
            node = nodes.pop( 0 )
            result.append( node.val )
            if node.next:
                nodes.append( node.next )

        print( result )

        for i, val in enumerate( result ):
            if val != result[len( result ) - 1 - i]:
                return False

        return True
