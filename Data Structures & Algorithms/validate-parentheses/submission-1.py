class Solution:
    def isValid(self, s: str) -> bool:
        d={
            '}':'{',
            ']':'[',
            ')':'('
        }
        a=[]
        for i in s:
            if i in d:
                if a and a[-1] == d[i]:
                    a.pop()
                else:
                    return False
            else:
                a.append(i)
        return True if not a else False
            