class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        first = 1
        second = 2
        for _ in range(3, n + 1):
            third = first + second
            first = second
            second = thrid
        return second