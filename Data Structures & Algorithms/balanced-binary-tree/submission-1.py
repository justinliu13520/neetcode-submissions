# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        if root.left is None and root.right is None:
            return True

        left_balance, right_balance = True, True
        if root.left:
            left_balance = self.isBalanced(root.left)
        if root.right:
            right_balance = self.isBalanced(root.right)
        

        left_depth = self.getDepth(root.left)
        right_depth = self.getDepth(root.right)
        
        print(root.val)
        if abs(left_depth-right_depth) > 1:
            print("entered")
            return False
        return right_balance and left_balance

    def getDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
        left = self.getDepth(root.left)
        right = self.getDepth(root.right)
        return 1 + max(left,right)