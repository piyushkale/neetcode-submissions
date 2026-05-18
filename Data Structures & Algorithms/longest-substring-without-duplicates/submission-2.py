class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        ns = ""
        m = 0

        for char in s:
            if char not in ns:
                ns+=char
            else:
                index = ns.find(char)
                ns = ns[index+1:]
                ns += char
            m = max(m,len(ns))    
        return m

