# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:

        def preorder(root):
            if not root:
                return ["#"]
            return [str(root.val)] + preorder(root.left) + preorder(root.right)
        return ",".join(preorder(root))
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        preorder_lst = data.split(",")
        self.root_idx = 0

        def build():
            if preorder_lst[self.root_idx] == "#":
                self.root_idx += 1
                return None
            root = TreeNode(int(preorder_lst[self.root_idx]))
            self.root_idx += 1
            root.left = build()
            root.right = build()
            return root
        return build()










