import collections


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_map = collections.Counter( s )
        t_map = collections.Counter( t )
        return s_map == t_map

