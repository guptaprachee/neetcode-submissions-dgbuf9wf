class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l=1
        r=max(piles)
        res=r
        while l<=r:
            temp=0
            mid =(r+l)//2
            for i in piles:
                temp+= math.ceil(i/mid)
            if temp<= h:
                res=min(res, mid)
                r=mid-1
            else:
                l=mid+1
        return res

        