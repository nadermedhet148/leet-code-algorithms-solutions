class Solution:
    
    def searchRange(self, nums, target):
        lo = 0
        hi = len(nums)
        first_index = -1
        last_index = -1
        while lo < hi:
            mid = (lo + hi) // 2
            print(mid , lo)
            if(nums[mid] == target):
                first_index = mid
                last_index = mid
                pass

            if(nums[mid] < target) : 
                lo +=1
            else :
                hi -= 1

        if(last_index == -1) :
            return [first_index,last_index]

        

        while last_index + 1 < len(nums) and nums[last_index + 1] == target:
            last_index +=1
        
        return [first_index,last_index]

class Solution2:
    def extreme_insertion_index(self, nums, target, left):
        lo = 0
        hi = len(nums)

        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] > target or (left and target == nums[mid]):
                hi = mid
            else:
                lo = mid+1

        return lo


    def searchRange(self, nums, target):
        left_idx = self.extreme_insertion_index(nums, target, True)
        if left_idx == len(nums) or nums[left_idx] != target:
            return [-1, -1]

        return [left_idx, self.extreme_insertion_index(nums, target, False)-1]

                
print(Solution().searchRange([5,7,7,8,8,8,8,8,10] , 8))