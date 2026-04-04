from collections import defaultdict

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # (0, 2), (2,0),(3, 4) , k =1, 
        # k smallest distance value --heap
        # coordinates and not the value

        minHeap =[]
        heapq.heapify(minHeap)
        h=defaultdict(list)
        result=[]
        for x, y in points:
            dist = math.sqrt(x**2 + y**2)
            heapq.heappush(minHeap, -dist)
            h[dist].append([x,y])

            if len(minHeap)>k:
                heapq.heappop(minHeap)
        #print(h, minHeap)
        for i in minHeap:
            #print(i)
            
            for j in h[-i]:
                if j not in result:
                    result.append(j)
        return  result


