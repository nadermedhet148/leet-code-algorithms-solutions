class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def maxPathSum(self, root):
        self.res = float('-inf')
        self.helper(root)
        return self.res 
        
    def helper(self, root):
        if not root:
            return 0
        left, right = self.helper(root.left), self.helper(root.right)
        self.res = max(self.res, root.val + left + right)
        return max(root.val + max(left, right), 0)