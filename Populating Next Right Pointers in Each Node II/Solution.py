from typing import List

class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        q = deque([root])
        while q:
            size = len(q)
            nxt = None
            for _ in range(size):
                node = q.popleft()
                node.next = nxt
                nxt = node
                if node.right:
                    q.append(node.right)
                if node.left:
                    q.append(node.left)
        return root