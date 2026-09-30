class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dif=defaultdict(int)
        for i in range(len(nums)):
            l= target-nums[i]
            if l in dif:
                return [dif[l],i]
            dif[nums[i]]=i
        return []
        