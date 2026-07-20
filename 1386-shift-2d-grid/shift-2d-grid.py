class Solution:
    def shiftGrid(self, grid, k):
        m, n = len(grid), len(grid[0])
        total = m * n
        flat = [grid[i][j] for i in range(m) for j in range(n)]
        k = k % total
        shifted = flat[-k:] + flat[:-k]
        new_grid = []
        for i in range(m):
            row = shifted[i*n:(i+1)*n]
            new_grid.append(row)
        return new_grid
