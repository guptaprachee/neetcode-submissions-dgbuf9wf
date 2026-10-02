class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-x for x in stones]
        heapq.heapify(max_heap)

        while len(max_heap)!=1:
            l1 = heapq.heappop(max_heap)
            l2 = heapq.heappop(max_heap)
            heapq.heappush(max_heap, l1 - l2)
        return -max_heap[0]



        
        

        