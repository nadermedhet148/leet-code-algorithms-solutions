from inspect import stack
from typing import List

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        lookup = [-1] * n
        stack = [0]
        numsDup = []
        i = 1
        while i < 2*n: 
            while stack and nums[i%n] > nums[stack[-1]]:
                lookup[stack[-1]] = nums[i%n]
                stack.pop()
            if lookup[i%n] == -1:
                stack.append(i%n)
            i += 1
        return lookup     

class Solution2:
    def findMaxLen(ob, S):
        if len(S) == 0:
            return 0
        stack = [-1]
        res = 0
        
        for i,c in enumerate(S):
            if c == '(':
                stack.append(i)
            else:
                stack.pop()
                
                if len(stack) == 0:
                    stack.append(i)
                else:
                    res = max(res,i-stack[-1])
        return res

Solution2().findMaxLen("()(())(")
                

nums1 = [4,1,2 ,3]
s = Solution()
print(s.nextGreaterElements(nums1))