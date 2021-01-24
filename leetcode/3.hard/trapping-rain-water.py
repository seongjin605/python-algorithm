from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        n = len( height )
        if n < 3:
            return 0
        left = 0
        right = n - 1
        left_max = height[0]
        right_max = height[n - 1]
        output = 0
        while left <= right:
            if left_max < right_max:
                output += left_max - height[left]
                left += 1
                if left == n:
                    break
                left_max = max( left_max, height[left] )
            else:
                output += right_max - height[right]
                right -= 1
                if right == -1:
                    break
                right_max = max( right_max, height[right] )
            return output

        '''
        height = [0,1,0,2,1,0,1,3,2,1,2,1]
                            L
                                R
        left_max = 2
        right_max = 3
        output = 6
        '''
