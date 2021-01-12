import collections

class TrieNode():
    def __init__(self, end=None, children=None):
        self.end = end
        if children is None:
            children = {}
        self.children = children
        
class Trie():
    def __init__(self):
        self.root = TrieNode()
        
    def add(self, word: str):
        ptr = self.root
        for ch in word:
            if ch not in ptr.children:
                ptr.children[ch] = TrieNode()
            ptr = ptr.children[ch]
        ptr.end = word
        
class Solution:
    def findSubstring(self, s: str, words):
        n = len(s)
        n_words = len(words)
        if n_words == 0:
            return []
        word_len = len(words[0])
        
        trie = Trie()
        counts = collections.Counter(words)
        for word in counts:
            trie.add(word)
                
        ptrs = []
        found = {}
        for i, ch in enumerate(s):
            ptrs2 = []
            ptrs.append(trie.root)
            for ptr in ptrs:
                if ch in ptr.children:
                    ptr2 = ptr.children[ch]
                    if ptr2.end is not None:
                        found[i-len(word)+1] = ptr2.end
                    else:
                        ptrs2.append(ptr2)
            ptrs = ptrs2
            
        res = []
        for i in range(n-word_len*n_words+1):
            if i not in found:
                continue
                
            counts2 = counts.copy()
            j = i
            while j in found and found[j] in counts2:
                counts2[found[j]] -= 1
                if counts2[found[j]] == 0:
                    del counts2[found[j]]
                j += word_len
                
            if len(counts2) == 0:
                res.append(i)
                
        return res

s =Solution()
print(s.findSubstring('barfoothefoobarman' , ["foo","bar"]))