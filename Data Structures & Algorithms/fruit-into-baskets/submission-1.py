class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # 0th -1, 1st-2 , 2nd-2
        # 2 baskets so , order of trees, 1,2,3,2,1,2,1,1 , (2,3)
        n=len(fruits)
        count = collections.defaultdict(int)
        l, total, res=0,0,0
        for r in range(n):
            count[fruits[r]]+=1
            total+=1
            while len(count)>2:
                f=fruits[l]
                count[f]-=1
                total-=1
                l+=1
                if not count[f]:
                    count.pop(f)

            res= max(res, total)
        return res

            


        