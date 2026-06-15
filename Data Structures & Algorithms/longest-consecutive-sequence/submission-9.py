class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if len(nums)==0:
            return 0
        m = 0
        curr = 0
        res = []
        ar = sorted(set(nums))

        for num in ar:
            if not res:
                res = [num]
                curr =1
                m =1
            elif (num - res[-1]) == 1:
                res.append(num)
                curr+=1
                m = max(m,curr)
            else:
                res = [num]
                curr = 1
        return m

        