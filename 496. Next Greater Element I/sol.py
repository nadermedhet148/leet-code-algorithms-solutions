from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        stack = []
        d = {}
        
        for e in nums2:
            
            while(stack and e > stack[-1]):
                c = stack.pop()
                d[c] = e
            
            stack.append(e)
        
        return [d.get(e, -1) for e in nums1]

nums1 = [4,1,2 ,3]
nums2 = [1,3,4,2]
s = Solution()
print(s.nextGreaterElement(nums1 , nums2))