class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sl, st=0,0
    
        while st< len(t) and sl<len(s):
            if s[sl] == t[st]:
                sl+=1
            st+=1
        return sl==len(s)
