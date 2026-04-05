class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        l=0
        window = maxwindow=0
        satisfied=0
        for r in range(len(customers)):
            if grumpy[r]:
                window+=customers[r]
            else:
                satisfied+=customers[r]
                
            if r-l+1 > minutes:
                if grumpy[l]:
                    window-=customers[l]
                l+=1
            maxwindow = max(window, maxwindow)
        return satisfied + maxwindow


        