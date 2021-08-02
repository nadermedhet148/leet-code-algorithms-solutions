# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """

        if not head:
            return None

        left, right = head, head
        stop = False
        def recurseAndReverse(right, m, n):
            nonlocal left, stop

            if n == 1:
                return

            right = right.next

            if m > 1:
                left = left.next

            recurseAndReverse(right, m - 1, n - 1)

            if left == right or right.next == left:
                stop = True

            if not stop:
                left.val, right.val = right.val, left.val

                left = left.next           

        recurseAndReverse(right, m, n)
        return head



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
