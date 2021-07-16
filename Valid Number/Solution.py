class Solution:
    def isNumber(self, s: str) -> bool:
        transition = {
            "":     {"num": "num",  ".": ".", "sign": "sign"},
            "num":  {"num": "num",  ".": ".num", "e": "e", "final": True},
            ".":    {"num": ".num"},
            ".num": {"num": ".num", "e": ".e", "final": True},
            ".e":   {"num": ".enum", "sign": ".enum"},
            ".enum":{"num": ".enum", "final": True},
            "e":    {"num": "enum", "sign": "esign"},
            "enum": {"num": "enum", "final": True},
            "esign":{"num": "enum"},
            "sign": {"num": "num",  ".": "."},
        }
        tokens = {str(i): "num" for i in range(10)} 
        tokens = {**tokens, "+": "sign", "-": "sign", "E": "e", "e": "e", ".": "."} 

        state = ""
        while s:
            c = s[:1]
            s = s[1:]

            if c not in tokens:
                return False
            token = tokens[c]

            if token in transition[state]:
                state = transition[state][token]
            else:
                return False

        return "final" in transition[state]

s = Solution()
print(s.isNumber("+2e3.4"))
print(s.isNumber("++2e3.4"))
print(s.isNumber("--2e3.4"))
print(s.isNumber("+-2e3.4"))
