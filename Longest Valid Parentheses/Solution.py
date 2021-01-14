from collections import defaultdict

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        length, curr = 0, 0
        h = defaultdict(int)
        for c in s:
            if c == '(':
                stack.append(c)
            else:
                if not stack:
                    h = defaultdict(int)
                    curr = 0
                else:
                    stack.pop()
                    h[len(stack)] += 2 + h[len(stack) + 1]
                    h[len(stack) + 1] = 0
                    curr = h[len(stack)]
                length = max(length, curr)
        return length




s = Solution()

print(s.longestValidParentheses(')()())'))