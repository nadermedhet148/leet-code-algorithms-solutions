from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m,n = len(matrix) , len(matrix[0])

        for i in range(m):
            if(matrix[i][n -1] >= target):
                for x in range(n):
                    if(matrix[i][x] == target):
                        return True
                return False
        
        return False
        

        



s = Solution()

print(
s.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]] , target = 3)
)