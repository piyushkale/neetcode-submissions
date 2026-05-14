class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}  # Initialize a regular dictionary
        for s in strs:
            sortedS = ''.join(sorted(s))  # Sort the string
            if sortedS not in res:  # Check if the key exists
                res[sortedS] = []  # If not, create a new list for this key
            res[sortedS].append(s)  # Append the original string to the list
        return list(res.values())  # Return the grouped anagrams as a list of lists
