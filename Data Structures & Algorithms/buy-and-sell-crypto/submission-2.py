class Solution:
    def maxProfit(self, p: List[int]) -> int:
        l, r = 0, 1
        maxp =0
        while l< r and r< len(p):
            maxp = max(maxp, p[r] - p[l])
            if p[r] <= p[l]:
                l=r
                r+=1
            else:
                r+=1
        return maxp
            
        