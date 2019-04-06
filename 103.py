该问题需要用到队列，与之前的二叉树的层次遍历类似，不同点在于在偶数层需要翻转一下。

建立一个queue
先把根节点放进去，这时候找根节点的左右两个子节点
去掉根节点，此时queue里的元素就是下一层的所有节点
循环遍历，将结果存到一个一维向量里
遍历完之后再把这个一维向量存到二维向量里
如果该层为偶数层，则reverse翻转一下
以此类推，可以完成层序遍历

from collections import defaultdict, deque

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        queue, alt = deque(), deque()

        queue.append(root)

        res = []
        current = []
        should_reverse = True
        while queue:
            node = queue.pop()
            current.append(node.val)
            if node.left:
                alt.appendleft(node.left)
            if node.right:
                alt.appendleft(node.right)

            if not queue:
                res.append(current[::-1] if should_reverse else current)
                current = []
                should_reverse = not should_reverse
                queue, alt = alt, queue

        return res
