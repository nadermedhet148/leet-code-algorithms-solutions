from typing import List

class Solution:
      def canJump(self, nums):
        last = len(nums)-1
        first = last-1
        while first >=0:
            if nums[first]+first >= last:
                last = first
                first-=1
            else:
                first-=1
        return last==0
        

s = Solution().canJump([3,2,1,0,4 , 1,1 , 1, 1,1,1])

print(s)