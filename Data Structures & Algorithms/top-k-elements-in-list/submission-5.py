
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Count frequencies
        counts = {}
        
        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1
        
        # Step 2: Sort the counts by frequency
        sorted_counts = sorted(counts.items(), key=lambda item: item[1], reverse=True)
        
        # Step 3: Extract the top k elements
        res = []
        for i in range(k):
            res.append(sorted_counts[i][0])  # Get the number, not the count
        
        return res
