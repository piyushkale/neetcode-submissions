class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        res = []
        n = len(nums)
        for i in range(n):
            t=1
            for j in range(n):
                if i!=j:
                    t*=nums[j]
            res.append(t)
        return res