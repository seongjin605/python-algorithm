# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# https://leetcode.com/problems/palindrome-linked-list/submissions/
# class Solution:
#     def isPalindrome(self, head: ListNode) -> bool:
#         if not head: return True

#         walker = head
#         runner = head
#         count = 0

#         while runner != None:
#             count += 1
#             runner = runner.next
#             if runner == None and count == 1: return True
#             if runner != None:
#                 runner = runner.next
#                 print( 'runner: ', runner )
#                 walker = walker.next
#                 print( 'walker: ', walker )
#                 if runner and walker and runner.val == walker.val:
#                     return True
#                 else:
#                     continue
#         return False

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import collections


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head: return True
        dq = collections.deque()
        dq.append(head)

        nodes = collections.deque()
        while len(dq) > 0:
            node = dq.popleft()
            nodes.append(node.val)
            if node.next:
                dq.append(node.next)

        while len(nodes) > 1:
            if nodes.popleft() != nodes.pop():
                return False

        return True


#         for i, val in enumerate(nodes):
#             print('val:', val)
#             if val != nodes[len(nodes) -i - 1]:
#                 return False

#         return True