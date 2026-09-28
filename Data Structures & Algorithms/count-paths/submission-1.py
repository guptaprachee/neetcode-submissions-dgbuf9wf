class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        mat = [[0 for i in range(n)] for j in range(m)]
        for i in range(m):
            mat[i][n-1]=1
        for j in range(n):
            mat[m-1][j]=1    
        for i in range(m-2, -1,-1):
            for j in range(n-2,-1,-1):
                mat[i][j]= mat[i+1][j]+ mat[i][j+1]

        return mat[0][0]
            

        