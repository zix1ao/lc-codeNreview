"""
Given a string s which consists of lowercase or uppercase letters,
return the length of the longest palindrome that can be built with those letters.
Letters are case-sensitive, for example, "Aa" is not considered a palindrome here.

Example 1:
Input: s = "abccccdd"
Output: 7
Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.

Example 2:
Input: s = "a"
Output: 1
Explanation: The longest palindrome that can be built is "a", whose length is 1.

Constraints:
  ·1 <= s.length <= 2000
  ·s consists of lowercase and/or uppercase English letters only.
"""


class Solution:
    def longestPalindrome(self, s: str) -> int:
        oddCount = 0
        ump = {}
        for ch in s:
            ump[ch] = ump.get(ch, 0) + 1
            if ump[ch] % 2 != 0:
                oddCount += 1
            else:
                oddCount -= 1

        if oddCount > 1:
            return len(s) - oddCount + 1

        return len(s)


if __name__ == "__main__":
    sol = Solution()
    print(sol.longestPalindrome("abccccdd"))