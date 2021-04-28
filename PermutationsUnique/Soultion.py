from typing import List
from collections import Counter
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        results = []
        def permute(comb, counter):
            if len(comb) == len(nums):
                results.append(list(comb))
                return

            for num in counter:
                if counter[num] > 0:
                    comb.append(num)
                    counter[num] -= 1
                    permute(comb, counter)
                    comb.pop()
                    counter[num] += 1

        permute([], Counter(nums))

        return results

print(Solution().permuteUnique([1,1,2]))