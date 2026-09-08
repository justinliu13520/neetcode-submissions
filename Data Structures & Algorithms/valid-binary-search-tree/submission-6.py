# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValid(self,root,leftBoundary,rightBoundary):
        if not root:
            return True
        # print(root.val,leftBoundary,rightBoundary)
        if root.left:
            # bigger than root
            if root.val <= root.left.val:
                return False
        #if right exists and is smaller than root
        if root.right:
            if root.val >= root.right.val:
                return False        
        if leftBoundary >= root.val or root.val >= rightBoundary:
            return False
        
        return self.isValid(root.left,leftBoundary,root.val) and self.isValid(root.right,root.val,rightBoundary)
        
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return self.isValid(root,float("-inf"),float("inf"))