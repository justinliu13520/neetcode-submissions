# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        def dfs(root,cur_good):
            nonlocal res
            if not root:
                return
            if root.val >= cur_good:
                res += 1
                cur_good = root.val
            dfs(root.left,cur_good)
            dfs(root.right,cur_good)
        dfs(root,root.val)
        return res