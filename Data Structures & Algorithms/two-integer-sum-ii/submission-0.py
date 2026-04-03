class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n=len(numbers)
        l=0
        r=n-1
        while l<r and r<= n-1:
            if numbers[l]+ numbers[r] == target:
                return [l+1,r+1]
            elif numbers[l] + numbers[r] <target:
                l+=1
            elif numbers[l] + numbers[r] >target:
                r-=1
            
        