import ast
from typing import List

# # 暴力解法 时间复杂度O（mn）
# class Solution:
#     def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
#         rows = len(matrix)
#         cols = len(matrix[0])
#
#         for i in range(rows):
#             for j in range(cols):
#                 if matrix[i][j] == target:
#                     return True
#
#         return False

# 右上角搜索
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix: return False

        rows = len(matrix)
        cols = len(matrix[0])

        i, j = 0, cols - 1

        while i < rows and j >= 0:
            x = matrix[i][j]
            if x == target:
                return True
            elif x > target:
                j -= 1
            else:
                i += 1

        return False



str = input().strip()
matrix = ast.literal_eval(str)
target = int(input())

solution = Solution()
print(solution.searchMatrix(matrix, target))
