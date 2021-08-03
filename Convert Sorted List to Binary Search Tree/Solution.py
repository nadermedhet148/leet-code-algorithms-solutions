class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        A, n = [], head
        while n:
            A.append(n.val)
            n = n.next
        def make(i,j):
            if i<=j:
                m       =  (i+j)//2
                n       = TreeNode(A[m])
                n.left  = make(i  ,m-1)
                n.right = make(m+1,j  )
                return n      

        return make(0,len(A) -1)