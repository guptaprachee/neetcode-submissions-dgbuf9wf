class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n=len(nums)
        result =[]
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            l= i+1 
            r= n-1
            while l <r :
                localsum= nums[l]+ nums[r] +nums[i]
                if localsum == 0:
                    result.append([nums[i], nums[l], nums[r]])
                    
                    while l<r and nums[l] == nums[l+1]:
                        l+=1
                    while l<r and nums[r]== nums[r-1]:
                        r-=1
                    l+=1
                    r-=1
                    
                elif localsum >0:
                    r-=1
                else:
                    l+=1
        return result 
        