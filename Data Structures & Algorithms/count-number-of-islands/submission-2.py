class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        row, col = len(grid), len(grid[0])
        visit = set()
        island=0

        def bfs(r, c):
            q= collections.deque()
            visit.add((r,c))
            q.append((r,c))
            while q:
                rows, cols = q.popleft()
                direction =[[1,0],[-1,0],[0,1],[0,-1]]

                for dr,dc in direction:
                    r,c = rows+dr, cols+dc
                    if r in range(row) and c in range(col) and (r,c) not in visit and grid[r][c] =="1":
                     visit.add((r,c))
                     q.append((r,c))




        for r in range(row):
            for c in range(col):
                if (r,c) not in visit and grid[r][c] =="1":
                    bfs(r,c)
                    island+=1
        return island
        