from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key=lambda x: x[0])

        merged = []
        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                x = merged[-1][1];
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged

s = Solution().merge([[8,10],[1,3],[2,6],[15,18]])
print(s)