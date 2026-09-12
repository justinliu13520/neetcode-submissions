# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = float("-inf")
        def dfs(root):
            nonlocal res
            if not root:
                return 0
            left = max(dfs(root.left),0)
            right = max(dfs(root.right),0)
            cur_val = left + root.val + right
            res = max(res,cur_val)

            return root.val + max(left,right)

        dfs(root)
        return int(res)