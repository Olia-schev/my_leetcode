class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        maxLocal = [[0 for _ in range(n - 2)] for _ in range(n - 2)]
        for i in range(1, n - 1):
            for j in range(1, n - 1):
                submatrix = [grid[i - 1][j - 1:j + 2], grid[i][j - 1:j + 2], grid[i + 1][j - 1:j + 2]]
                maxLocal[i - 1][j - 1] = max(max(row) for row in submatrix)
        return maxLocal


            
        