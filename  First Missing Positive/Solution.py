from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        if not nums:
            return 1
        else:
            max_range = max(nums)        
        
        if max_range <= 0 :
            return 1
        
        nums.sort()
        
        for i in range(1,max_range):
                if i not in nums:
                    return i
        return nums[-1] + 1