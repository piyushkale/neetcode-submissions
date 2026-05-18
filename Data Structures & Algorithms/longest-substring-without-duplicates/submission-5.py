class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        sr = set()

        l = 0
        res = 0
        for i in range(len(s)):
            while s[i] in sr:
                sr.remove(s[l])
                l+=1
            sr.add(s[i])
            res = max(res,i-l+1)
        return res
