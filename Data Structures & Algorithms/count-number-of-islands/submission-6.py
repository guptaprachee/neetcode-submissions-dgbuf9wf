class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visit =set()
        n,m=len(grid), len(grid[0])
        res=0
        def dfs(i,j):
            if i<0 or j<0 or i>= n or j>= m or grid[i][j]!="1":
                return 
            
            #visit.add((i,j))
            grid[i][j]='0'
            dist=[[i+1,j], [i-1, j], [i,j+1],[i,j-1]]
            for r,c in dist:
                dfs(r,c)
        
        for i in range(n):
            for j in range(m):
                if  grid[i][j]=="1":
                    res+=1
                    dfs(i,j)
                    
        return res



        