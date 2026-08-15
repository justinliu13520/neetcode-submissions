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
        q = deque([root])
        res = []
        height = 0
        while q:
            cur_len = len(q)
            level = []
            for node in q:
                if not node:
                    continue
                level.append(node.val)
            res.append(level)
            for _ in range(cur_len):
                if len(q) == 0:
                    break
                cur_node = q.popleft()
                if not cur_node:
                    continue
                q.append(cur_node.left)
                q.append(cur_node.right)
            height += 1
        while res[-1] == []:
            res.pop()
        return res
