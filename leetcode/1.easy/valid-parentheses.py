'class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        target = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        for c in s:
            if c not in target:
                stack.append(c)
            elif not stack or target[c] != stack.pop():
                    return False

        return len(stack) == 0
