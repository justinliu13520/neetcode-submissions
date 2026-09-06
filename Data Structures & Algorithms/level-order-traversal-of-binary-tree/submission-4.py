# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = []
        queue = deque([root])
        while queue:
            cur_layer = []
            # print(queue)
            while not queue[0]:
                queue.popleft()
                if len(queue) == 0:
                    break
            for _ in range(len(queue)):
                curr = queue.popleft()
                if not curr:
                    # queue.append(None)
                    continue
                cur_layer.append(curr.val)
                queue.append(curr.left)
                queue.append(curr.right)
            if len(cur_layer) > 0:
                res.append(cur_layer)
        return res

