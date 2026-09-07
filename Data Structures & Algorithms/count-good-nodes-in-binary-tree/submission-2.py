# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good_node = 0
        def dfs(root,val):
            nonlocal good_node
            if not root:
                return 0  
            if root.val >= val:
                print(root.val)
                good_node += 1
                val = root.val
            _ = dfs(root.left,val)
            _ = dfs(root.right,val)
            return good_node
        dfs(root,root.val)          
        return good_node