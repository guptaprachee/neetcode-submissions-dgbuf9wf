class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        d= defaultdict(list)
        for i,j in prerequisites:
            d[i].append(j)
        visit = set()
        def dfs(i):
            if i in visit:
                return False 
            if d[i] ==[]:
                return True
            
            visit.add(i)
            for j in d[i]:
                if not dfs(j):
                    return False
            visit.remove(i)
            d[i]=[]
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True


        