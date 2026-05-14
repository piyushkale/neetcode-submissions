class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        n_dict = {}

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in n_dict:
                return [n_dict[complement],i]
            n_dict[nums[i]] = i