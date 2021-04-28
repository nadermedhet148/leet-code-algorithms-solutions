from typing import List
class Solution:
    def jump(self, array: List[int]) -> int:
        minJumps = [float("inf") for _ in array]
        minJumps[0] = 0
        # O(n log n)
        for index in range(1, len(array)):
            for idx in range(index):
                if array[idx] >= index - idx:
                    minJumps[index] = min(minJumps[index], minJumps[idx] +1)
        print(minJumps)
        return minJumps[-1]



s = Solution().jump([2,3,1,1,4])
print(s)