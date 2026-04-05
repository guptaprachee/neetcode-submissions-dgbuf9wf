class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # num -> +ve 
        # min len subarray -> sum>=target else 0, best == target
        # maintain order

        # 2,1,5,1,5,3 -> 2,1,5,1,5 >target
        n=len(nums)
        l=0
        subsum=0
        arrayLen=float('inf')
        for r in range(n):
            subsum+= nums[r] #2, 3, 8, 9, 14 
            while subsum>= target:
                arrayLen=min(arrayLen, r-l+1)

                subsum-= nums[l] #14, 12, 11, 
                last =nums[l]
                l+=1
           
        return 0 if arrayLen== float('inf') else arrayLen
            

