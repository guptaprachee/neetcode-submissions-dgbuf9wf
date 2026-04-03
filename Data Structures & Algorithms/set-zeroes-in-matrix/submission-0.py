class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rowtop =False
        row = len(matrix)
        col= len(matrix[0])
        for i in range(row):
            for j in range(col):
                if matrix[i][j] ==0:
                    matrix[0][j] =0
                    
                    if i == 0:
                        rowtop=True
                    else:
                        matrix[i][0] =0
        print(matrix)
        for i in range(1, row):
            for j in range(1, col):
                print(matrix[i][j],matrix[i][0], matrix[0][j] )
                if matrix[i][0]==0 or matrix[0][j]==0:
                    matrix[i][j] =0

        if matrix[0][0]==0 :
            for i in range(row):
                matrix[i][0]=0
        if rowtop:
            for i in range(col):
                matrix[0][i]=0
        print(matrix)
        

                    
        