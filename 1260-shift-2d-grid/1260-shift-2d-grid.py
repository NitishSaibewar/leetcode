class Solution(object):
    def shiftGrid(self, grid, k):
        m = len(grid)
        n = len(grid[0])
        total = m * n
        k = k%total
        ans=[[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                idx = i * n+ j
                n_idx = (idx + k)% total
                n_row = n_idx//n
                n_col = n_idx % n
                ans[n_row][n_col] = grid[i][j]
        return ans