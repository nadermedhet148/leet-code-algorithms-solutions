from collections import defaultdict

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':

        if not head:
            return None

        dict_of_copy = {}

        cur = head
        while cur:
            dict_of_copy[ id(cur) ] = Node(x=cur.val, next=None, random=None)
            cur = cur.next

        cur = head
        while cur:

            if cur.next:
                dict_of_copy[ id(cur) ].next = dict_of_copy[ id(cur.next) ]

            if cur.random:
                dict_of_copy[ id(cur) ].random = dict_of_copy[ id(cur.random) ]

            cur = cur.next

        return dict_of_copy[ id(head) ]