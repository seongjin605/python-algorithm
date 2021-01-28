from typing import List

# https://leetcode.com/problems/array-partition-i/submissions/
'''
TC1 nums: [1,4,3,2]
TC2 nums: [6,2,6,5,1,2]
'''


def arrayPairSum(self, nums: List[int]) -> int:
    nums.sort()
    # 1. 오름차순해서 배열의 크기가 2가 될때마다 최소값을 합산처리 방식
    # sum = 0
    # arr = []
    # for n in nums:
    #     arr.append(n)
    #     if len(arr) == 2:
    #         sum += min(arr)
    #         while len(arr) > 0:
    #             arr.pop()
    # return sum

    # 2. 오름차순해서 어차피 index가 짝수번째만 합산(어차피 짝수 인덱스가 항상 작은값에 위치함)
    # sum = 0
    # for i, k in enumerate( nums ):
    #     if i % 2 == 0:
    #         sum += k
    # return sum

    # 3. 슬라이싱
    return sum( sorted( nums[::2] ) )