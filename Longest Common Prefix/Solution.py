class Solution:
    def longestCommonPrefix(self, strs):
        if not strs: return ""
        if len(strs) == 1: return strs[0]
        
        strs.sort()
        p = ""
        for x, y in zip(strs[0], strs[-1]):
            if x == y: p+=x
            else: break
        return r