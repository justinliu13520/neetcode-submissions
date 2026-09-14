# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        queue = deque([root])
        layers = []
        while queue:
            cur_layer = []
            for _ in range(len(queue)):
                cur_node = queue.popleft()
                if not cur_node:
                    continue
                cur_layer.append(cur_node.val)
                queue.append(cur_node.left)
                queue.append(cur_node.right)
            if len(cur_layer) > 0:
                layers.append(cur_layer)
        
        res = []
        for layer in layers:
            res.append(layer[-1])
        return res