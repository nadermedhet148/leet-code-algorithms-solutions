from typing import List

class Solution:
    def spiralOrder(self, n:int) -> List[List[int]]:

        matrix = [[0 for x in range(n)] for x in range(n)]
        counter = 1
        h = w = n
        if h < 1:
            return []

        # pointers we will use to iterate round the matrix
        top = 0
        bottom = h - 1
        left = 0
        right = w - 1

        while top <= bottom and left <= right:
    
            # TOP section: left to right
            l = left
            while l <= right:  # and left <= right: <-- we will never reach that condition
                matrix[top][l] = counter
                counter +=1
                l += 1
            # move lower
            # because: added all from the top area
            top += 1

            # RIGHT section: top to bottom
            t = top
            while t <= bottom:  # and top <= bottom: <-- we will never reach that condition
                matrix[t][right] = counter
                counter +=1
                t += 1
            # move pointer to the left
            # done with right-most section
            right -= 1

            # BOTTOM section: right to left
            # on the last of the spiral, char: right = left, therefore, r = left
            # so the while loop might run again
            r = right
            while r >= left and top <= bottom:
                matrix[bottom][r] = counter
                counter +=1
                r -= 1
            bottom -= 1

            # LEFT section: bottom to top
            # on the last of the spiral, char: bottom = top, therefore, b = top
            # so the while loop might run again
            # that's why we have the extra condition
            b = bottom
            while b >= top and left <= right:
                matrix[b][left] = counter
                counter +=1
                b -= 1
            left += 1

        return matrix
 
s = Solution().spiralOrder(5)
print(s)