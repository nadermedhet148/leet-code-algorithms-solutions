class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseList(self, head):
        prev = None
        while head:
            curr = head
            head = head.next
            curr.next = prev
            prev = curr
        return prev


        

othird = ListNode(4)
osecond = ListNode(3,othird)
ofirst = ListNode(1,osecond)

re = Solution().reverseList(ofirst)
re