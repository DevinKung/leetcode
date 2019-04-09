# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        #bfs
        result = [root.val]
        curLevel = [root]
        while curLevel:
            nextLevel = []
            for node in curLevel:
                if node.left:
                    nextLevel.append(node.left)
                if node.right:
                    nextLevel.append(node.right)
            curLevel = nextLevel
            if nextLevel: result.append(nextLevel[-1].val)
        return result