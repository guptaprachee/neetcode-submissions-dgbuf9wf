class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        if rows==1 and cols ==1:
            if target == matrix[0][0]:
                return True
            else:
                return False
        top, bot=0, rows-1
    
        while top <= bot:
            mid = (top+bot)//2
            if target > matrix[mid][-1]:
                top = mid + 1
            elif target < matrix[mid][0]:
                bot = mid - 1
            else:
                top = mid
                break
        
        if not (0 <= top < rows):
            return False

        l, r = 0, cols-1
        while l<= r:
            mid =(l+r)//2
            if target > matrix[top][mid]:
                l= mid +1
            elif target< matrix[top][mid]:
                r= mid-1
            else:
                return True

        return False
