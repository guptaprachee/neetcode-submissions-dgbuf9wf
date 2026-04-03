class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sl=0
        st=0
        if not s:
            return True
        while st< len(t):
            if s[sl] == t[st]:
                sl+=1
            if sl==len(s):
                return True

            st+=1
        return sl==len(s)
