class Solution:
    def isPalindrome(self, s: str) -> bool:
        finalstr= ''.join(c.lower() for c in s if c.isalnum())
        n=len(finalstr)
        l=0
        r=n-1
        while l<=r:
            if finalstr[l] != finalstr[r]:
                return False
            l+=1
            r-=1
        return True
                
            
            
    