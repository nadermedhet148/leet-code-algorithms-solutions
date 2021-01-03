# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        current_node = head
        while current_node :
            if current_node.next :
                temp = current_node.val
                current_node.val = current_node.next.val
                current_node.next.val = temp
                current_node = current_node.next.next
            else :
                current_node = current_node.next
        return head
                     