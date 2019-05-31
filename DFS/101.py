# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.helper(root.left,root.right)
    
    
    def helper(self,l,r):
        if not l and not r:
            return True
        if not l or not r:
            return False
        if l.val == r.val:
            outPair = self.helper(l.left,r.right)
            inPair = self.helper(l.right,r.left)
            return outPair and inPair
        else:
            return False