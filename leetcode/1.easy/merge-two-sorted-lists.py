# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Base Case
        if l1 == None:
            return l2
        if l2 == None:
            return l1

        # Recurson Relation
        node = ListNode( None )
        if l1.val < l2.val:
            node.val = l1.val
            node.next = self.mergeTwoLists( l1.next, l2 )
        else:
            node.val = l2.val
            node.next = self.mergeTwoLists( l1, l2.next )
        return node
        # if not l1 or (l2 and l1.val > l2.val):
        #     l1, l2 = l2, l1
        # if l1:
        #     l1.next = self.mergeTwoLists(l1.next, l2)
        # return l1
