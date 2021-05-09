class Solution:
    def recalCandidates(self, i: int, j: int):
        res = []
        for m in range(i+1, self.end+1): # for all subsequent rows
            diff = m - i
            if j in self.candidates[m]: # vertical downward
                self.candidates[m].remove(j)
                res += [(m, j)]
            if j-diff >= 0 and (j-diff) in self.candidates[m]: # left-downward
                self.candidates[m].remove(j-diff)
                res += [(m, j-diff)]
            if j+diff <= self.end and (j+diff) in self.candidates[m]: # right-downward
                self.candidates[m].remove(j+diff)
                res += [(m, j+diff)]
        return res
    def restoreCandidates(self, arr):
        for i,j in arr:
            self.candidates[i].add(j)
    def backtrack(self, currIdx: int):
        if currIdx == self.end: # end of chess board
            self.ans += 1
            return
        for i in self.candidates[currIdx]: # for all candidates in this row
            affected = self.recalCandidates(currIdx, i) # recalculate candidates and return affected cells
            if any([not i for i in self.candidates[currIdx+1:]]): # prune if any subsequent row has zero candidate, e.g. empty set
                self.restoreCandidates(affected)
                continue
            self.backtrack(currIdx+1)
            self.restoreCandidates(affected) # restore candidates
            
    def totalNQueens(self, n: int) -> int:
        self.ans = 0
        self.end = n-1
        # candidates store the candidates of each row in sets
        self.candidates = [set([i for i in range(n)]) for j in range(n)]
        self.backtrack(0)
        return self.ans

s = Solution().totalNQueens(4)
print(s)