# https://leetcode.com/problems/shuffle-string/
class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        arr = list(indices)
        for i, e in enumerate(indices):
            arr[e] = s[i]

        return ''.join(arr)