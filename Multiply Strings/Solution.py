class Solution(object):
    def multiply(self, s1, s2):
        s1, s2 = s1[::-1], s2[::-1]
        
        ans = 0
        tens_s1 = 1
        for digit1 in s1:
            tens_s2 = 1
            for digit2 in s2:
                ans += tens_s1 * (ord(digit1) - ord('0')) * tens_s2 * (ord(digit2) - ord('0'))
                tens_s2 *= 10
            tens_s1 *= 10
        return str(ans)

s = Solution()
s.multiply('123' , '321')