from typing import List

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle: 
            return 0
        if len(triangle) < 2:
            return triangle[0][0]
        if len(triangle) < 3:
            return triangle[0][0] + min(triangle[1])
        
        n, m = len(triangle), len(triangle[-1])
        
        dp = [[0] * (m) for i in range(n)]
        dp[0][0] = triangle[0][0]
        
        for i in range(1, n):
            dp[i][0] = triangle[i][0] + dp[i-1][0]
            
        for j in range(1, m):
            dp[j][j] = triangle[j][j] + dp[j-1][j-1]
            
        for i in range(2, n):
            for j in range(1, len(triangle[i])-1):
                dp[i][j] = min(dp[i-1][j], dp[i-1][j-1]) + triangle[i][j]
        
        return min(dp[m-1])

s = Solution()
s.minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]])