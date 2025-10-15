# 用bfs，队列中第 1 层和第 2 层的结点会紧挨在一起，无法区分。
# 因此，我们需要稍微修改一下代码，在每一层遍历开始前，记录队列中的结点数量 n，也就是这层的数目。
# 然后depth也要记得同步
from collections import deque

# 注意：由于可能存在无法被污染的橘子，我们需要记录新鲜橘子的数量。
# 在 BFS 中，每遍历到一个橘子（污染了一个橘子），就将新鲜橘子的数量减一。
# 如果 BFS 结束后这个数量仍未减为零，说明存在无法被污染的橘子。
class Solution:
    def orangeRotting(self,grid):
        m, n = len(grid), len(grid[0])
        fresh, time = 0, 0
        q = deque()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i, j)) # 语法易错点
                if grid[i][j] == 1:
                    fresh += 1
        # 方向
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        # bfs
        while q and fresh > 0:
            time += 1
            this_layer_num = len(q)
            for _ in range(this_layer_num):
                i, j = q.popleft()
                for x, y in directions: # 可以直接获取列表里的对
                    nx, ny = i + x, j + y
                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        fresh -= 1
                        q.append((nx, ny)) # 语法易错点
        return time if fresh == 0 else -1

m, n = map(int, input().split())
grid = []
for x in range(m):
    s = list(map(int, input().split()))
    grid.append(s)
solution = Solution()
print(solution.orangeRotting(grid))





