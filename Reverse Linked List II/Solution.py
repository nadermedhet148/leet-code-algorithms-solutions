# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
 
    def reverseBetween(self, head, m, n):
        if m == n:
            return head

        dummyNode = ListNode(0)
        dummyNode.next = head
        pre = dummyNode

        for i in range(m - 1):
            pre = pre.next
        
        # reverse the [m, n] nodes
        reverse = None
        cur = pre.next
        for i in range(n - m + 1):
            next = cur.next
            cur.next = reverse
            reverse = cur
            cur = next

        pre.next.next = cur
        pre.next = reverse

        return dummyNode.next



node7 = ListNode(8)
node6 = ListNode(7,node7)
node5 = ListNode(6, node6)
node4 = ListNode(5,node5)
node3 = ListNode(4,node4)
node2 = ListNode(3, node3)
node1 = ListNode(2,node2)
head = ListNode(1,node1)

s = Solution()
s.reverseBetween(head,3,7)
