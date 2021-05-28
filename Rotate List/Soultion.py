# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def cal_len(self, head):
        cur, count = head, 0
        while cur:
            count+=1
            cur = cur.next
        return count
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        l, cur = self.cal_len(head), head
        
        if l == 0 or l ==1 or k == 0:
            return head
        k = k%l
        if k ==0:
            return head
        for i in range(l-k-1):
            cur = cur.next
            
        a,b = cur.next,cur.next
        cur.next = None
        while b.next:
            b = b.next
        b.next = head
        return a

node3 = ListNode(1)
node2 = ListNode(2 , node3)
node = ListNode(3, node2)

s = Solution().rotateRight(node,2)