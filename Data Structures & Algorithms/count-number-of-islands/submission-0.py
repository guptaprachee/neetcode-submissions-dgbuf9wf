class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def dfs(r,c):
            if r<0 or c<0 or r>=row or c>=column or grid[r][c]!="1":
                return 
            else:
                grid[r][c]='0'
                dfs(r,c+1)
                dfs(r+1,c)
                dfs(r,c-1)
                dfs(r-1,c)
        num_islands=0
        row =len(grid)
        column=len(grid[0])
        for r in range(row):
            for c in range(column):
                if grid[r][c]=="1":
                    num_islands+=1
                    dfs(r,c)
        return num_islands
            