"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return None
        queue = [root]
        while queue:
            cur = queue.pop(0)
            if cur.left and cur.right:
                cur.left.next = cur.right
                cur.right.next = cur.next and cur.next.left
                queue.append(cur.left)
                queue.append(cur.right)
        return root