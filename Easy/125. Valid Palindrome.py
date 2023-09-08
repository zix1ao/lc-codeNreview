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


class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        :param s: str
        :return: bool
        """

        """
        This is a pretty straightforward problem. We are given a
        string and we have to determine if it reads the same forward
        and backward after converting all uppercase letters into 
        lowercase letters and removing all non-alphanumeric characters.
        For this problem, we could simply use list comprehension to
        divide the string into a list of characters and check whether
        it is the same forward and backward. Or, we could create an
        empty string and iterate through the input string to check
        if the character is alpha-numeric. If it is, append that
        character to the empty string we just created. Finally we
        just check if it is palindrome like before.
        """

        # s = [char.lower() for char in s if char.isalnum()]
        pal = ""
        for c in s:
            if c.isalnum():
                pal += c.lower()

        # return s == s[::-1]
        return pal == pal[::-1]


if __name__ == "__main__":
    sol = Solution()
    print(sol.isPalindrome("0P"))
