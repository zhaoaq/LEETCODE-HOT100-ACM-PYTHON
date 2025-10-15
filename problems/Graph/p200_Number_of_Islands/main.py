# ACM:
# 4 5
# 11110
# 11010
# 11000
# 00000
class Solution:
    def numIsland(self, grid):
        if not grid or not grid[0]:
            return 0

        count = 0
        m, n = len(grid), len(grid[0]) # m: 4 n: 5

        def dfs(i, j):
            # Over boundry or sea, skip
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != '1':
                return
            # Turn this area to land.
            grid[i][j] = '0'
            dfs(i - 1, j)
            dfs(i + 1, j)
            dfs(i, j - 1)
            dfs(i, j + 1)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    count += 1
                    dfs(i, j)

        return count


solution = Solution()
m, n = map(int, input().split())
grid = []
for x in range(m):
    s = list(input().strip()) #split() 会按空格分割字符串，没有空格没法分割
    grid.append(s)
print(solution.numIsland(grid))

