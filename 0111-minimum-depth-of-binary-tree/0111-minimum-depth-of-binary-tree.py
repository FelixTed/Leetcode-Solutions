# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        lengths = set()
        self.dfs(root,0,lengths)
        if lengths:
            return min(lengths)
        return 0

    def dfs(self,root, branchLength,lengths):
        if root is None:
            return
        branchLength += 1
        if root.left is not None:
            self.dfs(root.left,branchLength,lengths)
        if root.right is not None:
            self.dfs(root.right,branchLength,lengths)
        if root.right is None and root.left is None:
            lengths.add(branchLength)

            

        