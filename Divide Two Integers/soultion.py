class Solution:
    def _divide(self, dividend: int, divisor: int):
        
        if dividend < divisor:  
            return 0, dividend
        if dividend == divisor: 
            return 1, 0
        if divisor < dividend and dividend < divisor + divisor:
            return 1, dividend - divisor
        
        result, mod = self._divide(dividend, divisor + divisor)
        # Bitwise operators act on operands as if they were strings of binary digits. They operate bit by bit, hence the name.
        result = result << 1
        
        if mod >= divisor:
            mod -= divisor
            result += 1
            
        return result, mod
    
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == 0:
            return 0
                
        if divisor == 1:
            if dividend == 2147483648:
                return 2147483647
            
            return dividend
            
        if dividend < 0:
            if divisor < 0:
                return self.divide(-dividend, -divisor)
            
            return -self.divide(-dividend, divisor)
        
        if divisor < 0:
            return -self.divide(dividend, -divisor)
            
            return dividend
        
        result, mod = self._divide(dividend, divisor)
        
        return result
