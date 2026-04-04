from collections import defaultdict

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # (0, 2), (2,0),(3, 4) , k =1, 
        # k smallest distance value --heap
        # coordinates and not the value
        minHeap=[]
        for x,y in points:
            dist =x**2 + y**2
            minHeap.append([dist, x, y])
        heapq.heapify(minHeap)
        result=[]
        while k>0:
            dist, x, y= heapq.heappop(minHeap)
            result.append([x,y])
            k-=1
        return result
               


