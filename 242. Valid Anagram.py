"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false

Constraints:
  ·1 <= s.length, t.length <= 5 * 104
  ·s and t consist of lowercase English letters.
"""
from collections import defaultdict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 1st approach
        # for c in s:
        #     if set(s) == set(t) and len(s) == len(t) and s.count(c) == t.count(c):
        #         return True
        #     return False

        # 2nd approach
        count = defaultdict(int)

        for c in s:
            count[c] += 1

        for c in t:
            count[c] -= 1

        for val in count:
            if val != 0:
                return False

        return True

        # 3rd approach
        # return sorted(s) == sorted(t)


if __name__ == "__main__":
    sol = Solution()
    print(sol.isAnagram("anagram", "nagaram"))
