class Codec:
    def serialize(self, root: Optional[TreeNode]) -> str:
        vals = []
        def preorder(node):
            if not node:
                vals.append("#")
                return
            vals.append(str(node.val))
            preorder(node.left)
            preorder(node.right)
        preorder(root)
        return ",".join(vals)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = data.split(",")
        self.i = 0
        def build():
            val = vals[self.i]
            self.i += 1
            if val == "#":
                return None
            node = TreeNode(int(val))
            node.left = build()
            node.right = build()
            return node
        return build()