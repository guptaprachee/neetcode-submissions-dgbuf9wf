class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_rs, result = nums[0],0
        
        for i in nums:
            if result <0 :
                result =0
            result+=i
            max_rs= max(max_rs, result)
        return max(max_rs, result)