"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters
and removing all non-alphanumeric characters, it reads the same forward and backward.
Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Example 3:
Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.

Constraints:
  ·1 <= s.length <= 2 * 105
  ·s consists only of printable ASCII characters.
"""


import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # s = [char.lower() for char in s if char.isalnum()]
        pal = ""
        for i in s:
            if i.isalpha() or i in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                pal += i.lower()

        return s == s[::-1]




if __name__ == "__main__":
    sol = Solution()
    print(sol.isPalindrome("0P"))
