class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        num_sum = sum(nums)
        n=len(nums)
        print(num_sum)
        left =0
        for i in range(n):
            if num_sum-nums[i] ==left:
                return i
            left += nums[i]
            num_sum -= nums[i]
        return -1