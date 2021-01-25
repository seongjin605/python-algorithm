from typing import List

# https://leetcode.com/problems/trapping-rain-water/
class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len( height ) - 1

        left_max = 0
        right_max = height[right]

        result = 0

        while left <= right:
            if left_max <= right_max:
                result += left_max - height[left]
                left += 1
                if left == len( height ):
                    break
                left_max = max( left_max, height[left] )
            else:
                result += right_max - height[right]
                right -= 1
                if right == 0:
                    break
                right_max = max( right_max, height[right] )

        return result

    '''
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
                        L
                            R
    left_max = 2
    right_max = 3
    output = 6
    '''
