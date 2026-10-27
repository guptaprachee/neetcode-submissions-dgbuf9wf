class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana = defaultdict(list)

        for i in strs:
            count =[0]*26
            for c in i:
                count[ord(c)-ord("a")] +=1
            ana[tuple(count)].append(i)
        return list(ana.values())
            