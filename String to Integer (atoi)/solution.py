import unittest

class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.replace(' ' , '')
        if(s == ''):
            return 0
        first_char = s[0]
        is_neg = 0
        is_pos = 0
        num = 0

        if(first_char == '+'):
            is_pos = 1
        if(first_char == '-'):
            is_neg = 1
        if(not first_char.isnumeric() and first_char != "-" and first_char != "+" and first_char != ' '):
            return 0
        
        for ch_index in range(0,len(s) - (is_neg + is_pos)):
            ch = s[ch_index + (is_neg + is_pos)]
            if(ch.isnumeric()):
                num = (num *10) + int(ch)
            else:
                break;
        if(is_neg):
            num *= -1
        
        if(num < 0 and num < pow(-2,31)):
            return -2147483648
        if(num > 2147483647):
            return 2147483647
        return num 
        
        


class TestSolution(unittest.TestCase):

    # def test_start_with_first_word(self):
    #     s = Solution()
    #     self.assertEqual(s.myAtoi('words and 987'),0)
    # def test_positive_numeric(self):
    #     s = Solution()
    #     self.assertEqual(s.myAtoi('42'),42)
    # def test_negative_numeric(self):
    #     s = Solution()
    #     self.assertEqual(s.myAtoi('-42'),-42)
    # def test_negative_numeric_spaces(self):
    #     s = Solution()
    #     self.assertEqual(s.myAtoi('   -42'),-42)
    def test_numeric_wth_last_words(self):
        s = Solution()
        self.assertEqual(s.myAtoi('4193 with words'),4193)



if __name__ == '__main__':
    unittest.main()