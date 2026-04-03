class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n=len(nums)
        j=n-1
        for i in range(n-2, -1, -1):
            if nums[i] >= j-i:
                j=i
        
            
        return j ==0
        