# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        stack = []
        # stores the first half
        
        n = 0
        cur = head
        # get length
        while cur: 
            cur = cur.next
            n += 1
        
        cur = head
        for x in range(n//2):
            stack.append(cur.val)
            cur = cur.next
        
        if n % 2: cur = cur.next
        
        while cur:
            if stack[-1] != cur.val: return False
            stack.pop()
            cur = cur.next
        
        return True

fourth = ListNode(1);
third = ListNode(2, fourth);
second = ListNode(2, third);
first = ListNode(1 , second);

print(Solution().isPalindrome(first))
