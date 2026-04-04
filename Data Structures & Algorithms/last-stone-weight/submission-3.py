class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-n for n in stones]  

        heapq.heapify(max_heap)
        while len(max_heap)>1:
            s1= - heapq.heappop(max_heap)
            print(max_heap)
            s2= - heapq.heappop(max_heap)
            if s1<s2:
                heapq.heappush(max_heap, -(s2-s1))
            elif s1>s2:
                heapq.heappush(max_heap, -(s1-s2))

        return -max_heap[0] if len(max_heap)>0 else 0
        
        