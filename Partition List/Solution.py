class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:

        before = before_head = ListNode(0)
        after = after_head = ListNode(0)

        while head:
            if head.val < x:
                before.next = head
                before = before.next
            else:
                after.next = head
                after = after.next

            head = head.next

        after.next = None
        before.next = after_head.next

        return before_head.next



node7 = ListNode(1)
node6 = ListNode(6,node7)
node5 = ListNode(2, node6)
node4 = ListNode(3,node5)
node3 = ListNode(5,node4)
node2 = ListNode(4, node3)
node1 = ListNode(2,node2)
head = ListNode(1,node1)


s = Solution()
r = s.partition(head, 3)

r