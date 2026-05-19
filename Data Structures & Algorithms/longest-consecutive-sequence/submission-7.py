class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        ar = sorted(set(nums))

        res = 0
        r = []
        if len(nums)==0:
            return 0
        
        m = 0
        for num in ar:
            if not r:
                r.append(num)
                res+=1
                m=1
            elif (num - r[-1]) == 1:
                
                res+=1
                m = max(m,res)
                r.append(num)
            else:
                res = 1
                r = [num]
        return m
            
            

