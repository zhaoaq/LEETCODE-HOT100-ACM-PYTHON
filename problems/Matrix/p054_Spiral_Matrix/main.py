# 边界收缩法
# 1. 定义边界：使用四个变量l(left), r(right), t(top), b(bottom)来表示当前未遍历的矩阵边界。
# 2. 按层遍历：从外到内一层一层地遍历矩阵。
# 3. 方向顺序：按照右→下→左→上的顺序遍历每一层。
import ast
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]):
        res = []

        if not matrix:
            return res

        left = 0
        right = len(matrix[0]) - 1
        top = 0
        bottom = len(matrix) - 1

        while True:
            for i in range(left, right + 1):
                res.append(matrix[top][i])
            top += 1
            if top > bottom: break

            for i in range(top, bottom + 1):
                res.append(matrix[i][right])
            right -= 1
            if right < left: break

            for i in range(right, left - 1, -1):
                res.append(matrix[bottom][i])
            bottom -= 1
            if bottom < top: break

            for i in range(bottom, top - 1, -1):
                res.append(matrix[i][left])
            left += 1
            if right < left: break

        return res

str = input().strip()
matrix = ast.literal_eval(str)
# print(matrix)

solution = Solution()
print(solution.spiralOrder(matrix))