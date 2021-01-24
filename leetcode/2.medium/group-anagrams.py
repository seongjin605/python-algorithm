import collections
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words = collections.defaultdict( list )

        for word in strs:
            words[''.join( sorted( word ) )].append( word )

        return words.values()


