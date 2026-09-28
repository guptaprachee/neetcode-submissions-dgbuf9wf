class Solution:
    def climbStairs(self, n: int) -> int:
        if n<4:
            return n
        l=2
        r=3
        count =0
        
        for i in range(3,n):
            count =l+r
            l=r
            r=count
        return count
