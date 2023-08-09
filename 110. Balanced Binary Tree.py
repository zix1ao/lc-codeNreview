"""
Given a binary tree, determine if it is height-balanced.

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: true
Example 2:


Input: root = [1,2,2,3,3,null,null,4,4]
Output: false
Example 3:

Input: root = []
Output: true


Constraints:

The number of nodes in the tree is in the range [0, 5000].
-104 <= Node.val <= 104v
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: [TreeNode]) -> bool:
        return self.check(root) != -1

    def check(self, root):
        if not root:
            return 0

        left = self.check(root.left)
        right = self.check(root.right)

        if left == -1 or right == -1 or abs(left - right) > 1:
            return -1

        maximum = max(left, right)

        return maximum + 1






if __name__ == "__main__":
    sol = Solution()
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    print(sol.isBalanced(root))
