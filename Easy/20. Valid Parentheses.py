"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

An input string is valid if:
    1. Open brackets must be closed by the same type of brackets.
    2. Open brackets must be closed in the correct order.
    3. Every close bracket has a corresponding open bracket of the same type.

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

Constraints:
  ·1 <= s.length <= 10^4
  ·s consists of parentheses only '()[]{}'.
"""


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        """
        The problem is asking us to check whether the input string is valid.
        In other words, does the open bracket closed with the same type of
        brackets and in the correct order and has a corresponding closing bracket
        of the same type?
        We could consider using stack to solve this problem since stack follows the
        FILO(First In Last Out) principle. Firstly, we create a empty stack and then
        check if each character of the string is in the open bracket group, i.e. '([{'.
        If it is, append that character to the stack. Otherwise, in another if-else
        conditional, check whether the stack is empty. If it is, then there is no way
        this closing bracket has a corresponding open bracket. Otherwise, pop the
        topmost character from the stack and compare it accordingly. Finally, after
        traversing the whole string, if the stack is empty, then return true.
        """

        stack = []  # Stack

        for c in s:
            '''
            My approach of switching cases:

            if c == '(':
                stack.append('(')
            elif c == '[':
                stack.append('[')
            elif c == '{':
                stack.append('{')

            A better and simple approach:

            if c in '([{':
                stack.append(c)

            '''

            if c in '([{':
                stack.append(c)
            else:
                if len(stack) == 0:  # To improve this line, use 'if not stack'
                    return False
                else:
                    ob = stack.pop()  # Opening Bracket
                    if (ob == '(' and c != ')') or \
                        (ob == '[' and c != ']') or \
                        (ob == '{' and c != '}'):
                        return False

        '''
        My approach of checking if the stack is empty:
            
            if len(stack) == 0:
                return True
            
        A better and simple approach:
            
            return not stack
            
            (If the stack is empty, it will return True.
            Otherwise, it will return False.)
        
        '''
        return not stack


if __name__ == '__main__':
    s = Solution()
    print(s.isValid("({[]})"))
