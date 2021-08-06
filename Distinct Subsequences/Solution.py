class Solution:
    def numDistinct(self, s, t):
        l1, l2 = len(s)+1, len(t)+1
        dp = [[1] * l2 for _ in range(l1)]
        for j in range(1, l2):
            dp[0][j] = 0
        for i in range(1, l1):
            for j in range(1, l2):
                dp[i][j] = dp[i-1][j] + dp[i-1][j-1]*(s[i-1] == t[j-1])
                print(dp[i-1][j] + dp[i-1][j-1]*(s[i-1] == t[j-1]) , dp[i-1][j] , dp[i-1][j-1],(s[i-1] == t[j-1]) , s[i-1] , t[j-1])
        return dp[-1][-1]

s = Solution()
s.numDistinct("babag" , "bag")