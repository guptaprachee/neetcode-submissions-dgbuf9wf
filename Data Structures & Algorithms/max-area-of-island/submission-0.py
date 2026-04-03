class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])

        def dfs(r,c):
            if r<0 or c<0 or r>=row or c>=col or grid[r][c]==0:
                return 0
            grid[r][c]=0

            return (1+ dfs(r,c+1)+dfs(r+1,c)+dfs(r-1,c)+dfs(r,c-1))
        max_area=0
        for r in range(row):
            for c in range(col):
                if grid[r][c]==1:
                    curr_area= dfs(r,c)
                    max_area=max(max_area, curr_area)
        return max_area
        