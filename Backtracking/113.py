# Backtracking
# Time: O(n)
# Space: O(nlogn)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root:
            return []
        result = []
        self.helper(root,sum,[],result)
        return result
    
    def helper(self,root,target,path,result):
        if not root.left and not root.right and root.val == target:
            path.append(root.val)
            result.append(path)
        if root.left:
            self.helper(root.left,target-root.val,path+[root.val],result)
        if root.right:
            self.helper(root.right,target-root.val,path+[root.val],result)