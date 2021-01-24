from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}
        for i, value in enumerate( nums ):
            if target - value in nums_map:
                return i, nums_map[target - value]
            else:
                nums_map[value] = i
        print( nums_map )


