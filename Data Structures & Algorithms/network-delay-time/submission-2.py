class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges= defaultdict(list)

        for s,e,t in times:
            edges[s].append((e,t))
        
        visit =set()
        minheap=[(0,k)]
        t=0
        while minheap:
            w1, n1 = heapq.heappop(minheap)
            if n1 in visit :
                continue

            visit.add(n1)
            t=w1
            for n2,w2 in edges[n1]:
                if n2 not in visit:
                    heapq.heappush(minheap, (w1+w2, n2))

        return t if len(visit) == n else -1
        

