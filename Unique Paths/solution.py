class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = [[0 for i in range(n)] for x in range(m)]
        

        for i in range(n) :
         
            for j in range(m):
                if(i ==0 and j == 0) :
                    memo[j][i] = 1
                    continue
                top = left =  0
                if(i-1 >=0) :
                    top =  memo[j][i-1]
                if(j - 1 >=0) :
                    left =  memo[j-1][i]
                memo[j][i] = top + left
        return memo[m-1][n-1]



s = Solution().uniquePaths(3, 7)

print(s)