class Solution:
    def letterCombinations(self, digits):
        phone = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}
        combinationsDigest = list()
        combinationsList = list()

        for letter in range(0, len(digits)):
            combinationsDigest.append(phone[digits[letter]])

        for letterList in combinationsDigest:
            combinationsList = self.combinList(combinationsList,letterList)

        return combinationsList

    def combinList(self,list1 , list2) : 
        combinedList = list()
        if(len(list1) == 0):
            return list2
        for x in list1:
            for y in list2:
                combinedList.append(x+y)
        return combinedList
s = Solution()
print(s.letterCombinations("235"))