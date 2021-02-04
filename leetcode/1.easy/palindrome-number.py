# https://leetcode.com/problems/palindrome-number/submissions/
class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_str = str(x)
        for i, val in enumerate(x_str):
            if val != x_str[len(x_str) - 1 - i]:
                return False
        return True
