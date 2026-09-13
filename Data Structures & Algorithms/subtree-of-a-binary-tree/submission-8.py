# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def serialize(self, root: Optional[TreeNode]) -> str:
        preorder_lst = []
        def preorder(root):
            if not root:
                preorder_lst.append("#")
                return
            preorder_lst.append(str(root.val))
            preorder(root.left)
            preorder(root.right)
        preorder(root)
        return ",".join(preorder_lst)    
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        root_str = self.serialize(root)
        subRoot_str = self.serialize(subRoot)
        return subRoot_str in root_str




