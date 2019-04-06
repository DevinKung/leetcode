class Solution(object):
  def levelOrderBottom(self, root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """
    res,data=[],[]
    if not root:return res
    stack=[]
    stack.append(root)
    nCount=1#记录每层节点数
    while stack:
        node=stack.pop(0)
        data+=[node.val]#保存每层节点的值
        nCount-=1
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
        if nCount==0:
            res=[data]+res
            data=[]
            nCount=len(stack)
    return res
