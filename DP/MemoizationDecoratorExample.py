class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        d = {}
        def memoization_decorator(func):
            def wrapper(a, b):
                if (a, b) not in d:
                    d[(a,b)] = func(a,b)
                return d[(a, b)]
            return wrapper
        @memoization_decorator
        def recursion(i, j):
            if i==m-1 and j==n-1:
                return grid[i][j]
            else:
                if i+1<m:
                    down = grid[i][j] + recursion(i+1, j)
                else:
                    down = float("inf")
                if j+1<n:
                    right = grid[i][j] + recursion(i, j+1)
                else:
                    right = float("inf")
                return min(down, right)
        return recursion(0,0)