from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        res = []

        h = len(matrix)
        if h < 1:
            return res
        w = len(matrix[0])

        # pointers we will use to iterate round the matrix
        top = 0
        bottom = h - 1
        left = 0
        right = w - 1

        while top <= bottom and left <= right:

            # TOP section: left to right
            l = left
            while l <= right:  # and left <= right: <-- we will never reach that condition
                res.append(matrix[top][l])
                l += 1
            # move lower
            # because: added all from the top area
            top += 1

            # RIGHT section: top to bottom
            t = top
            while t <= bottom:  # and top <= bottom: <-- we will never reach that condition
                res.append(matrix[t][right])
                t += 1
            # move pointer to the left
            # done with right-most section
            right -= 1

            # BOTTOM section: right to left
            # on the last of the spiral, char: right = left, therefore, r = left
            # so the while loop might run again
            r = right
            while r >= left and top <= bottom:
                res.append(matrix[bottom][r])
                r -= 1
            bottom -= 1

            # LEFT section: bottom to top
            # on the last of the spiral, char: bottom = top, therefore, b = top
            # so the while loop might run again
            # that's why we have the extra condition
            b = bottom
            while b >= top and left <= right:
                res.append(matrix[b][left])
                b -= 1
            left += 1

        return res
 
s = Solution().spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]] )