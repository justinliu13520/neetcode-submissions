# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
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
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        decoded = data.split(",")
        print(decoded)
        self.root_index = 0
        def build():
            cur_val = (decoded[self.root_index])
            self.root_index += 1
            if cur_val == "#":
                return None
            root = TreeNode(int(cur_val))
            root.left = build()
            root.right = build()
            return root
        return build()

