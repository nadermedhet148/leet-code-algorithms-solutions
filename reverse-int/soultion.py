# class Solution:
#     def reverse(self, x) -> int:
#         a = str(abs(x));
#         rev_a = a[::-1]
#         rev_x = int(rev_a)
#         if(x < 0):
#             rev_x = rev_x * -1
#         return rev_x

  

class Solution:
    def reverse(self, x: int) -> int:
        num = 0
        a = abs(x)
        while(a != 0):
            pop = a % 10
            num = num * 10 + pop
            a = int(a / 10)
            print(a,pop , num)
        if x > 0 and num < 2**31:
            return num
        elif x < 0 and num <= 2**31:
            return -num
        else:
            return 0
        
              

s = Solution()
print(s.reverse(1029))