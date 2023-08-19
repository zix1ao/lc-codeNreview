"""
Given two strings s and t, return true if they are equal when both are typed into empty text editors.
'#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

Example 1:
Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both s and t become "ac".

Example 2:
Input: s = "ab##", t = "c#d#"
Output: true
Explanation: Both s and t become "".

Example 3:
Input: s = "a#c", t = "b"
Output: false
Explanation: s becomes "c" while t becomes "b".

Constraints:
  ·1 <= s.length, t.length <= 200
  ·s and t only contain lowercase letters and '#' characters.
"""


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stackS, stackT = [], []

        for c in s:
            if c != '#':
                stackS.append(c)
            elif len(stackS) > 0:
                stackS.pop()

        for c in t:
            if c != '#':
                stackT.append(c)
            elif len(stackT) > 0:
                stackT.pop()

        if stackS == stackT:
            return True

        return False


if __name__ == "__main__":
    sol = Solution()
    print(sol.backspaceCompare("a##c", "#a#c"))