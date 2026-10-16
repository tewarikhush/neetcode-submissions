# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
      
        q = collections.deque()
        q.append(root)
        while len(q):
            level_size = len(q)
            level = []
            for i in range(level_size):
                current_level = q.popleft()
                if current_level:
                    q.append(current_level.left)
                    q.append(current_level.right)
                    level.append(current_level.val)
            if level:
                res.append(level)
        return res