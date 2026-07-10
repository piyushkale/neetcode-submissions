class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts_c = {}
        for num in nums:
            if num not in counts_c:
                counts_c[num]=0
            counts_c[num]+=1
        
        l = sorted(counts_c.items(), key=lambda x:x[1],reverse=True)
        res = []
        for i in range(k):
            res.append(l[i][0])
        return res