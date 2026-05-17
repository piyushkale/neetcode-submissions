class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        res = [0,0]
        d= {}

        for i in range(len(numbers)):
            c= target-numbers[i]
            if c in d and d[c]!=i:
                
                return [d[c]+1,i+1]
            d[numbers[i]]=i

        