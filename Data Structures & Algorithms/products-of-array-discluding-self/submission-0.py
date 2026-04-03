class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        output =[1 for i in range(n)]
        prev =1

        for i in range(n-1):
            output[i+1]= nums[i] *prev
            prev =prev *nums[i]
        prev=1
        for j in range(n-1, 0, -1):
            output[j-1] = output[j-1]* nums[j]* prev
            prev =prev*nums[j]
        return output
        