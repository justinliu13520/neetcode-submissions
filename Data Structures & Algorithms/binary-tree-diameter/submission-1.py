class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0
        
        def getHeight(node):
            if not node:
                return 0
            
            # Recursively get the height of left and right subtrees
            left_h = getHeight(node.left)
            right_h = getHeight(node.right)
            
            # The diameter at THIS node is left_h + right_h
            self.max_diameter = max(self.max_diameter, left_h + right_h)
            
            # Return the height of this node to the caller (parent)
            return 1 + max(left_h, right_h)
        
        getHeight(root)
        return self.max_diameter