class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_collection = {}

        for ele in strs:
            nstring = "".join(sorted(ele))
            if nstring not in anagram_collection:
                anagram_collection[nstring] = []
            anagram_collection[nstring].append(ele)

       

        return list(anagram_collection.values())
