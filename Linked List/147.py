# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        p = dummy = ListNode(0)
        cur = head
        p.next = head
        while cur and cur.next:
            if cur.val <= cur.next.val:
                cur = cur.next
                continue
            
            while p.next.val < cur.next.val:
                p = p.next
            new = cur.next
            cur.next = new.next
            new.next = p.next
            p.next = new
            p = dummy
        return dummy.next