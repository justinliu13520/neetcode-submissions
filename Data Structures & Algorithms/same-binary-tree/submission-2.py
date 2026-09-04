# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        p_queue = deque()
        p_queue.append(p)
        p_res = []
        q_queue = deque()
        q_queue.append(q)
        q_res = []

        while p_queue:
            curr = p_queue.popleft()
            if curr is None:
                p_res.append(None)
                continue
            p_res.append(curr.val)
            p_queue.append(curr.left)
            p_queue.append(curr.right)
        while q_queue:
            curr = q_queue.popleft()
            if curr is None:
                q_res.append(None)
                continue
            q_res.append(curr.val)
            q_queue.append(curr.left)
            q_queue.append(curr.right)
        print(q_res,p_res)
        return q_res == p_res
