from collections import defaultdict 
from typing import List

class Solution(object):
    def groupAnagrams(self, strs):
        ans = defaultdict(list)
        for s in strs:
            ans[tuple(sorted(s))].append(s)
        return ans.values()

s = Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"])
