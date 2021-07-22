# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        sentailNode =  ListNode(0 , head)
        pred = sentailNode
        
        while head:
            if head.next and head.val == head.next.val:
                while head.next and head.val == head.next.val:
                    head = head.next
                pred.next = head.next 
            else:
                pred = pred.next 
                
            head = head.next
            
       
          
        return sentailNode.next


s = Solution()
node7 = ListNode(4)
node6 = ListNode(3,node7)
node5 = ListNode(2, node6)
node4 = ListNode(2,node5)
node3 = ListNode(1,node4)
node2 = ListNode(1, node3)
node1 = ListNode(1,node2)
head = ListNode(0,node1)



s.deleteDuplicates(head)
        