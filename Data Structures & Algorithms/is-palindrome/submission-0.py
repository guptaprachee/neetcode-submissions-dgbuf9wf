class Solution:
    def isPalindrome(self, s: str) -> bool:
        finalstr= ''.join(c.lower() for c in s if c.isalnum())
        n= len(finalstr)
        for i in range(n):
            print(finalstr[i], finalstr[n-1-i])
            if finalstr[i] != finalstr[n-1-i]:
                return False
        return True
