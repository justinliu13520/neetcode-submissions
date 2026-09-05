# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        if not subRoot:
            return True
        
        if self.isSameTree(root,subRoot):
            return True
        else:
            return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)
    def isSameTree(self,tree1,tree2):
        if not tree1 and not tree2:
            return True
        if tree1 and not tree2:
            return False
        if tree2 and not tree1:
            return False
        if tree1.val != tree2.val:
            return False
        else:
            return self.isSameTree(tree1.left,tree2.left) and self.isSameTree(tree1.right,tree2.right)