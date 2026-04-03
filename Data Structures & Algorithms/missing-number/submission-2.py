class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total= sum(range(len(nums)+1))
        for i in nums:
            total -= i
        return total
        