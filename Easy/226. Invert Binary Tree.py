"""
Given the root of a binary tree, invert the tree, and return its root.

Example 1:
Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]

Example 2:
Input: root = [2,1,3]
Output: [2,3,1]

Example 3:
Input: root = []
Output: []

Constraints:
  ·The number of nodes in the tree is in the range [0, 100].
  ·-100 <= Node.val <= 100
"""
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: [TreeNode]) -> [TreeNode]:
        """
        :param root: [TreeNode]
        :return: [TreeNode]
        """

        """
        This is a binary tree problem. We are given the root of
        a binary tree. All we have to do is to invert this tree
        so that every left and right subtree is swapped. 
        We can use recursion to solve this problem. First let's
        consider the base case. If the current tree node is empty,
        then we return null. Otherwise, we call our function and
        traverse the left and right subtree recursively. Assign the
        left subtree to the right and vice versa. Noted that swapping
        should be done at the same time or we will assign the value
        of say the updated left subtree to the right subtree, which
        is the same.
        """


        if not root:
            return None
        self.invertTree(root.left)
        self.invertTree(root.right)

        root.left, root.right = root.right, root.left

        # left = root.left
        # right = root.right
        # root.left = self.invertTree(right)
        # root.right = self.invertTree(left)

        return root

    def level_order_traversal(self, root):
        if not root:
            return []

        result = []
        queue = deque([root])

        while queue:
            node = queue.popleft()
            if node:
                result.append(node.val)
                queue.append(node.left)
                queue.append(node.right)

        return result


if __name__ == "__main__":
    sol = Solution()
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(9)

    root = sol.invertTree(root)

    print(sol.level_order_traversal(root))
