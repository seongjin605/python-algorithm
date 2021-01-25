from typing import List

# https://leetcode.com/problems/container-with-most-water/
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len( height ) - 1
        left_loc, right_loc = 0, 0
        left_max, right_max = height[left], height[right]
        result = 0

        while left <= right:
            if left_max < right_max:
                left_max = max( left_max, height[left] )
                left += 1
                left_loc += 1
            else:
                right_max = max( right_max, height[right] )
                right -= 1
                right_loc += 1

        # width = min()
        print( 'left_max:', left_max )
        print( 'right_max:', right_max )

        print( 'right:', right )
        print( 'left:', left )

        return result

