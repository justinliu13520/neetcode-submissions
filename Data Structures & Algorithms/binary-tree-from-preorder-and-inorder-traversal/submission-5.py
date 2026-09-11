# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_dict = {val:idx for idx,val in enumerate(inorder)}

        self.prefix_index = 0
        def pre_inorder(l,r):
            if l > r:
                return None
            root = TreeNode(preorder[self.prefix_index])
            self.prefix_index += 1
            mid = inorder_dict[root.val]
            root.left = pre_inorder(l,mid-1)
            root.right = pre_inorder(mid+1,r)
            return root
        return pre_inorder(0,len(inorder) - 1)