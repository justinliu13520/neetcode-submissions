# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def in_ordrr(root):
            if not root:
                return []
            return in_ordrr(root.left) + [root.val] + in_ordrr(root.right)
        res = in_ordrr(root)
        print(res)
        return res[k-1]

