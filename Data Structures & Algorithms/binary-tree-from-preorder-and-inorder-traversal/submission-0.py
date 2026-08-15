# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # This stores the index of the values found in inorder so we can grab them right away instead
        # of looping every time
        indices = {val: idx for idx, val in enumerate(inorder)}

        # Tracks the index of the pre order we're looking at
        self.pre_idx = 0
        def dfs(l, r):
            if l > r:
                return None

            root_val = preorder[self.pre_idx]
            self.pre_idx += 1
            root = TreeNode(root_val)
            # mid is the root of tree/subtree. This will split into left and right subtree in array
            mid = indices[root_val] 
            # Sets the left and then right subtree
            root.left = dfs(l, mid - 1)
            root.right = dfs(mid + 1, r)
            # returns the children node of the previous call all the way back up
            return root

        # We start with 0 because that's the index root of the whole tree with pre order
        return dfs(0, len(inorder) - 1)