#range(rows-1, 0, -1)
# 参数含义：
# rows-1：遍历的起始索引（矩阵最后一行的索引）
# 0：遍历的结束索引（不包含 0，实际到索引 1 为止）
# -1：步长（每次递减 1，即从后往前遍历）

# any()函数：这是 Python 的内置函数，用于判断可迭代对象中是否存在至少一个元素为真（True）。
# 如果存在，则返回 True；否则返回 False。

# 二维数组读入：使用 ast.literal_eval() 安全地将字符串转换为Python列表
import ast
from typing import List



class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        cols = len(matrix[0])

        # 拿出两个量作为首行首列0情况的标志
        first_row_zero_flag = False
        first_col_zero_flag = False

        # 查看首行首列是否有0
        first_row_zero_flag = any(matrix[0][i] == 0 for i in range(cols))
        first_col_zero_flag = any(matrix[j][0] == 0 for j in range(rows))

        # 用首行首列作其他元素的标志
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0

        # 根据标志操作 反循环数组（防止破坏首行首列的标志）
        for i in range(rows - 1, 0, -1):
            for j in range(cols - 1, 0, -1):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0

        # 根据flag置首行首列为0
        if first_row_zero_flag == True:
            for i in range(cols):
                matrix[0][i] = 0
        if first_col_zero_flag == True:
            for j in range(rows):
                matrix[j][0] = 0

str = input().strip()
matrix = ast.literal_eval(str)
#print(len(matrix))

solution = Solution()
solution.setZeroes(matrix)
print(matrix)