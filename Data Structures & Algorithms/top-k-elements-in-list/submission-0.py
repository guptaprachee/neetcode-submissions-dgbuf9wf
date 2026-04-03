class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        d={}

        for n in nums:
            if n in d:
                d[n]+=1
            else:
                d[n]=1
        largest_keys = sorted(d, key=d.get, reverse=True)[:k]
        return largest_keys

        