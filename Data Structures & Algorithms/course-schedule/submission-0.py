class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap= collections.defaultdict(list)
        for cr, re in prerequisites:
            preMap[cr].append(re)
        
        visit =set()
        def dfs(cr):
            if cr in visit:
                return False
            if preMap[cr]==[]:
                return True
            visit.add(cr)
            for i in preMap[cr]:
                if not dfs(i):
                    return False
            visit.remove(cr)
            preMap[cr]=[]
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
        