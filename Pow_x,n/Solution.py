class Solution(object):
    def myPow(self, x, n):
        if n == 0:
            return 1
        if n < 0:
            return self.myPow(1/x, -n) 
        partial = self.myPow(x, n // 2)
        result = partial * partial
        
        if (n % 2) == 1: 
            result *= x
        return result
print( Solution().myPow(2.00000 , -2))