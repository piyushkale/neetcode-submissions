class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        
        set_str = set()
        m=0
        l=0
        for i in range(len(s)):
            while s[i] in set_str:
                set_str.remove(s[l])
                l+=1
            set_str.add(s[i])
            m = max(m,i-l+1)
        return m