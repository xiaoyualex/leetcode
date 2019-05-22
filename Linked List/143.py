# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return 
        head, middle = self.splitList(head)
        middle = self.reverseList(middle)
        head = self.mergeList(head,middle)
        
        
    def splitList(self, head):
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        middle = slow.next
        slow.next = None
        return head, middle
    
    def reverseList(self, head):
        prev = None
        cur = head
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        return prev
    
    def mergeList(self,a,b):
        head = a
        while b:
            next1, next2 = a.next, b.next
            a.next = b
            b.next = next1
            a, b = next1, next2
        return head