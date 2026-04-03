class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n=len(heights)
        vol=0
        for i in range(n):
            for j in range(i+1,n):
                vol = max(vol, min(heights[j], heights[i])*(j-i))
        return vol
