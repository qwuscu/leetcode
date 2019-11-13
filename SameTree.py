# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        # both p and q are None
        if not p and not q:
            return True
        if p and q and p.val == q.val:
            return self.isSameTree(p.right, q.right) and self.isSameTree(p.left, q.left)
        return False