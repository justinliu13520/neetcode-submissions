# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root.right and not root.left:
            return 1
        gNodes = 1
        def dfs(root: TreeNode, curMax: int):
            nonlocal gNodes
            if not root:
                return
            if root.val >= curMax:
                curMax = root.val
                gNodes += 1
            dfs(root.right,curMax)
            dfs(root.left,curMax) 
        dfs(root.right,root.val)
        dfs(root.left,root.val)
        return gNodes