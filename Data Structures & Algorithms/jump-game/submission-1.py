class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        failed = set()          # indices we already know are dead ends

        def dfs(i):
            if i >= n - 1:      # reached (or passed) the last index
                return True
            if i in failed:     # already proved this spot can't win
                return False
            for step in range(1, nums[i] + 1):   # your "one branch per step" idea
                if dfs(i + step):
                    return True
            failed.add(i)
            return False

        return dfs(0)