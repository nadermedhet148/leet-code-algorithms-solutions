class Solution:
    def minPathSum(self, grid) -> int:
        m = len(grid)
        n = len(grid[0])
        memo = [[0 for i in range(n)] for x in range(m)]
        for i in range(n) :
            for j in range(m):
                if(i ==0 and j == 0) :
                    memo[j][i] = grid[0][0]
                    continue
                down = right = 1e100
                if(i-1 >=0) :
                    right =  memo[j][i-1] + grid[j][i]
                if(j - 1 >=0) :
                    down =  memo[j-1][i] + grid[j][i]
                memo[j][i] = min(right , down)
        return memo[m-1][n-1]

s = Solution().minPathSum([[1,2,3],[4,5,6]])
print(s)