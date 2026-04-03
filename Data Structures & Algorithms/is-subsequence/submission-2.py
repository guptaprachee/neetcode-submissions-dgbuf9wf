class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sl=0
        st=0
        c=0
        if not s:
            return True
        while st< len(t):
            if s[sl] == t[st]:
                c+=1
                sl+=1
            if c==len(s):
                return True

            st+=1
        return c==len(s)
