class Solution:

    def encode(self, strs: List[str]) -> str:
        newStr=""
        
        for s in strs:
            newStr += str(len(s))+ "#"+s
            
        return newStr


    def decode(self, s: str) -> List[str]:
        i=0
        n=len(s)
        result=[]
        while i< n:
            j =i
            while s[j]!= "#" :
                j+=1
            length= int(s[i:j])
            i=j+1
            j=i+ length
            result.append(s[i:j])
            i=j
        return result