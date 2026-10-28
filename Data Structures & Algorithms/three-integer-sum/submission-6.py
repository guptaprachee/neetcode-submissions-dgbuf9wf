class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res =[]
        n= len(nums)
        nums.sort()
        for i in range(n):
            if i >0 and nums[i-1] == nums[i]:
                continue
            l= i+1
            r= n-1
            
            while l < r:
                if nums[i]+ nums[l] +nums[r] ==0:
                    res.append([nums[i], nums[l], nums[r]])
                    while l<r and nums[l+1] == nums[l]:
                        l+=1
                    while l<r and nums[r-1] == nums[r]:
                        r-=1
                    l+=1
                    r-=1
                elif nums[l] +nums[r] + nums[i] >0:
                    r-=1
                else:
                    l+=1
        return res

        