class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        # max k increment 
        # 1,2,10 -- k =4 [2,2,10], sorted?
        n= len(nums)
        nums.sort()
        count=0
        l=0
        total=0
        for r in range(n):
            total+=nums[r]
            while nums[r]*(r-l+1) > total+k:
                total -= nums[l]
                l+=1
            count = max(count, r-l+1)

            
                
        return count

            




            


        