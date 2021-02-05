from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []
        def helper(i, path):
            if sum(path) == target:
                results.append(path[:])
                return 
			
            if sum(path) > target:
                return 
			
            for x in range(i, len(candidates)):
                path.append(candidates[x])
                helper(x, path)
                path.pop()

        helper(0, [])
        return results
            



s = Solution()
print(s.combinationSum([2,3,6,7],7))