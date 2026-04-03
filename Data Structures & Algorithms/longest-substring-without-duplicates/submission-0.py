class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # abcdeblpmo
        charset=set()
        left =0
        maxL=0
        for r in range(len(s)):
            while s[r] in charset:
                charset.remove(s[left])
                left+=1
            charset.add(s[r])
            maxL= max(maxL, len(charset))
        return maxL
        