class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        new= set()
        for i in nums:
            if i in new:
                return i
            new.add(i)
        return -1
        