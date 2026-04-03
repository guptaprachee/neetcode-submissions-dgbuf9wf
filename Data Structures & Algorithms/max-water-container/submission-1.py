class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left , right =0, len(heights)-1
        maxres =0
        while left <= right:
            area= (right -left)*min(heights[left], heights[right])
            maxres=max(maxres, area)
            if heights[left] < heights[right]:
                left+=1
            else:
                right-=1
        return maxres

        