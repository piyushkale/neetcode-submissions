class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n_arr = set()
        for element in nums:
            if element in n_arr:
                return True
            n_arr.add(element)
        return False