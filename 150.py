# -*- coding: utf-8 -*-
#用数据结构栈来解决这个问题。

#从前往后遍历数组
#遇到数字则压入栈中
#遇到符号，则把栈顶的两个数字拿出来运算，把结果再压入栈中
#遍历完整个数组，栈顶数字即为最终答案

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        S = []
        OP = {'+': lambda x, y: x + y,
             '-': lambda x, y: x - y,
             '*': lambda x, y: x * y,
             '/': lambda x, y: x // y if x // y > 0 else -(abs(x) // abs(y))}
        for token in tokens:
            if token in OP:
                R = S.pop()
                L = S.pop()
                S.append(OP[token](L, R))
            else:
                S.append(int(token))
        return S[-1]
        