"""
Given two strings ransomNote and magazine,
return true if ransomNote can be constructed by using the letters from magazine and false otherwise.
Each letter in magazine can only be used once in ransomNote.

Example 1:
Input: ransomNote = "a", magazine = "b"
Output: false

Example 2:
Input: ransomNote = "aa", magazine = "ab"
Output: false

Example 3:
Input: ransomNote = "aa", magazine = "aab"
Output: true

Constraints:
  ·1 <= ransomNote.length, magazine.length <= 105
  ·ransomNote and magazine consist of lowercase English letters.
"""
from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag = {}

        for c in magazine:
            if c not in mag:
                mag[c] = 1
            else:
                mag[c] += 1

        for c in ransomNote:
            if c not in mag:
                return False
            else:
                mag[c] -= 1
                if mag[c] < 0:
                    return False

        return True


if __name__ == "__main__":
    sol = Solution()
    print(sol.canConstruct("aa", "aab"))