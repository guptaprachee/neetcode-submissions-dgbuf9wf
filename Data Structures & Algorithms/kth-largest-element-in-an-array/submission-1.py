class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # unsorted - nlogn , a[k]
        # OR ELSE heap
        maxHeap =[]
        for i in nums:
            heapq.heappush(maxHeap, i)
            if len(maxHeap)>k:
                heapq.heappop(maxHeap)
        return maxHeap[0]

