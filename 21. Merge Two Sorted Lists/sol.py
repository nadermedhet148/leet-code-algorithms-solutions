# Definition for singly-linked list.
from soupsieve import select


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, a, b):
        if not a or b and a.val > b.val:
            a,b = b,a
        if a :
            a = self.mergeTwoLists(a.next , b)
        return
        
        


othird = ListNode(4)
osecond = ListNode(3,othird)
ofirst = ListNode(1,osecond)


sthird = ListNode(4)
ssecond = ListNode(2,sthird)
sfirst = ListNode(1,ssecond)

s = Solution().mergeTwoLists(ofirst,sfirst)