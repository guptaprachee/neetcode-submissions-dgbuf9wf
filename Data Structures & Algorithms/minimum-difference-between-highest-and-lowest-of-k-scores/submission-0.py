class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        l=0
        r= k-1
        mindiff = nums[len(nums)-1]-nums[0]

        while r< len(nums):
            mindiff = min(nums[r]-nums[l], mindiff)
            r+=1
            l+=1
        return mindiff
             
