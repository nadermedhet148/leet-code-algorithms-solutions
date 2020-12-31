class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s;

        rows = list()
        for _ in range(numRows):
            rows.append('')
        
        curRow = 0
        goingDown = False

        for c in s:
            rows[curRow] = rows[curRow] + c
            if (curRow == 0 or curRow == numRows - 1):
                goingDown = not goingDown;
            if(goingDown):
                curRow +=1
            if(not goingDown):
                curRow +=-1
        
        returnedString = ''
        for row in rows:
            returnedString += row

        return returnedString
s= Solution()
print(
s.convert('AB' , 1)
)