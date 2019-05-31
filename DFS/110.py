# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        if abs(self.getMaxHeight(root.left)- self.getMaxHeight(root.right)) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)
        
    
    
    def getMaxHeight(self,node):
        if not node:
            return 0
        return 1 + max(self.getMaxHeight(node.left),self.getMaxHeight(node.right))
        