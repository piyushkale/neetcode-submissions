class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        n = {}

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in n:
                return [n[complement],i]
            n[nums[i]] = i