class Solution(object):
    def runningSum(self, nums):
        arr = []
        lastSum = 0 
        for item in nums:
            lastSum +=item
            arr.append(lastSum)

        return arr

            



print(Solution().runningSum([1,1,1,1,1]))