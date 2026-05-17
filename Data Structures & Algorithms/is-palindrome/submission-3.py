class Solution:
    def isPalindrome(self, s: str) -> bool:
         # Convert the string to lowercase and filter out non-alphabetic characters
        filtered_s = "".join(char.lower() for char in s if char.isalnum())

        # Check if the filtered string is equal to its reverse
        return filtered_s == filtered_s[::-1]