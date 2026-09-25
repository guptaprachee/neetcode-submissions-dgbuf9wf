class Solution:
    def isValid(self, s: str) -> bool:
        d={')':'(', ']':'[','}':'{'}
        n=len(s)
        i=0
        if n <2:
            return False
        cur= []
        for i in range(n):
            if s[i] in d :
                if d[s[i]] in cur and cur[-1] == d[s[i]]:
                    cur.pop()
                else:
                    return False
            else:
                cur.append(s[i])
            
        return len(cur) ==0
        