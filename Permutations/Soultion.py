from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.result = []
        def perm(nums, res):
            if not nums:
                self.result.append(res)
            for i in range(len(nums)):
                perm(nums[ : i] + nums[i + 1 : ], res + [nums[i]])
        perm(nums, [])
        return self.result
s = Solution().permute([5,4,6,2])

print(s)