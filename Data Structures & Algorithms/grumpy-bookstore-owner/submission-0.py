class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        l=0
        r= minutes-1
        n=len(customers)
        maxres=0
        while r< n:
            total =0
            for i in range(n):
                if i>=l and i<=r:
                    total+= customers[i]
                elif grumpy[i]==0:
                    total+= customers[i]
            maxres=max(maxres, total)
            l+=1
            r+=1
        return maxres


        