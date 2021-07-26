from typing import List

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        currentIndex = 0

        res = []

        while currentIndex < len(words):
            totalChars = 0;
            mergedWords = []
            for i in range(currentIndex , len(words)):
                totalChars += len(words[i])
                if(totalChars + len(mergedWords) < maxWidth ):
                    mergedWords.append(words[i])
                    currentIndex += 1
                else:
                    totalChars -= len(words[i])
                    break;
            freeSpace = maxWidth - totalChars;
            spaceLength = freeSpace 
            if(len(mergedWords) > 2) :
                spaceLength = int(round( freeSpace / (len(mergedWords) - 1)))
            newWord = ""
            for mergedWord in mergedWords:
                newWord = newWord +  mergedWord + "".join([" " for _ in range(spaceLength) ]) 
                freeSpace -= spaceLength;
                if(spaceLength > freeSpace):
                    spaceLength = freeSpace

            res.append(newWord)


        return res
                
                    
                


s = Solution()

print(s.fullJustify(["This", "is", "an", "example", "of", "text", "justification."],16))


