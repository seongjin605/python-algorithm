import collections
from typing import List

# https://leetcode.com/problems/group-anagrams/
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words = collections.defaultdict( list )

        for word in strs:
            words[''.join( sorted( word ) )].append( word )

        return words.values()


