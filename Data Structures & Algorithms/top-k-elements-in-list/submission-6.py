class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        counts = {}

        for num in nums:
            if num not in counts:
                counts[num] = 1
            else:
                counts[num] += 1

        sorted_Counts = sorted(counts.items(), key=lambda items: items[1], reverse=True)

        res = []

        for i in range(k):
            res.append(sorted_Counts[i][0])
        
        return res