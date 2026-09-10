# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # This solution is optimized to use a hashmap to grab the index fast. The one thing about this is
        # we need to keep track of the boundaries in our subarray. So instead of passing in the whole subarray, we can use the l and r as boundaries and keep a global index for the preorder index that we were
        # using as the root

        indices = {val:idx for idx,val in enumerate(inorder)}

        self.preorder_index = 0

        def dfs(l,r):
            if l > r:
                return None

            root = TreeNode(preorder[self.preorder_index]) # make the root with the first preorder in the current recursion
            self.preorder_index += 1 # increment to know we are looking at the next root next time
            mid = indices[root.val]
            root.left = dfs(l,mid-1)
            root.right = dfs(mid+1,r)
            return root


        return dfs(0,len(inorder)-1)