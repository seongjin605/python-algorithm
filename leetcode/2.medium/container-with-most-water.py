from typing import List

# https://leetcode.com/problems/container-with-most-water/
'''
length: 오른쪽 x좌표 - 왼쪽 x좌표
width: 왼쪽 y좌표 또는 오른쪽 y좌표의 최소값

최대 너비 공식: width * length 
'''
def maxArea(self, height: List[int]) -> int:
    left, right = 0, len( height ) - 1
    max_sum = 0

    while left < right:
        max_sum = max( max_sum, min( height[left], height[right] ) * (right - left) )
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_sum