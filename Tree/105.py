# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if inorder:
            root_ind = inorder.index(preorder.pop(0))
            root = TreeNode(inorder[root_ind])
            root.left = self.buildTree(preorder,inorder[:root_ind])
            root.right = self.buildTree(preorder,inorder[root_ind+1:])
            return root
        else:
            return None
        