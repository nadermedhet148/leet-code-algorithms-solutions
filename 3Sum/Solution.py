class Solution:
    def threeSum(self, nums):
        triplets = []
        nums.sort()
        
        for i in range(len(nums)-2):
            cur, seen, used = nums[i], {}, set()
            if cur > 0: break
            if i > 0 and cur == nums[i-1]: continue
            for j in range(i+1, len(nums)):
                if nums[j] in seen and nums[j] not in used:
                    triplets.append([cur,seen[nums[j]],nums[j]])
                    used.add(nums[j])
                else:
                    seen[-(cur+nums[j])] = nums[j]
        print(seen,used)
        return triplets


s = Solution()
print(s.threeSum([0,0,0]))
        
        
print()        