# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        if not root:
            return res
        
        q = [root]
        while q:
            r = [c.val for c in q]
            res.append(r)
            qq = []
            for c in q:
                if c.left: qq.append(c.left)
                if c.right: qq.append(c.right)
            q = qq
        return res
