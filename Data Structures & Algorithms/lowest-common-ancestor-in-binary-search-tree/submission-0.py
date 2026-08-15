# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        curr = root
        
        while curr:
            # If both are in the right subtree
            if p.val > curr.val and q.val > curr.val:
                curr = curr.right
            # If both are in the left subtree
            elif p.val < curr.val and q.val < curr.val:
                curr = curr.left
            # We found the split point (or found p or q)
            else:
                return curr