import ast


class Solution:
    def rotateMatrix(self, matrix):
        #注意这个题目下矩阵都是方阵
        n = len(matrix)

        for i in range(n // 2):
            for j in range((n + 1) // 2):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[n - j - 1][i]
                matrix[n - j - 1][i] = matrix[n - i - 1][n - j - 1]
                matrix[n - i - 1][n - j - 1] = matrix[j][n - i - 1]
                matrix[j][n - i - 1] = tmp


str = input().strip()
matrix = ast.literal_eval(str)

solution = Solution()
solution.rotateMatrix(matrix)
print(matrix)

