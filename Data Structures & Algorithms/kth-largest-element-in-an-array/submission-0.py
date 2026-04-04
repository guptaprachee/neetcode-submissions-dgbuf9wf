class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # unsorted - nlogn , a[k]
        # OR ELSE heap
        heapq.heapify(nums)
        while len(nums)>k:
            heapq.heappop(nums)
        return nums[0]

