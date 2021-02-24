# https://leetcode.com/problems/integer-replacement
class Solution:
    def integerReplacement(self, n: int) -> int:
        if n == 1: return 0

        count = 0

        is_odd = n % 2 == 1

        if is_odd:
            n = n + 1
            count = count + 1

        while n != 1:
            n = n / 2
            count = count + 1

        return count
