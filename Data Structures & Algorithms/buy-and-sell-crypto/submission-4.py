class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        l=0
        r=1
        macp=0
        while l<r and r<n:
            if prices[l]< prices[r]:
                macp = max(macp, prices[r]-prices[l])
                
            else:
                l=r
            r+=1
        
        return macp


        