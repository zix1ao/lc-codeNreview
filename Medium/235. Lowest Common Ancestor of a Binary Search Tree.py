"""
Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.
According to the definition of LCA on Wikipedia:
“The lowest common ancestor is defined between two nodes p and qas the lowest node in T
that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Example 1:
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.

Example 2:
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.

Example 3:
Input: root = [2,1], p = 2, q = 1
Output: 2

Constraints:
  ·The number of nodes in the tree is in the range [2, 105].
  ·-109 <= Node.val <= 109
  ·All Node.val are unique.
  ·p != q
  ·p and q will exist in the BST.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        :param root: 'Treenode'
        :param p: 'TreeNode'
        :param q: 'TreeNode'
        :return: 'TreeNode'
        """

        """
        This is a easy medium problem as long as we know how binary search tree works.
        We are given a binary search tree (BST) called root and two nodes called p and q.
        We have to find the lowest common ancestor (LCA) node of two given nodes in the
        BST. The lowest common ancestor is defined between two nodes p and q as the lowest
        node in T that has both p and q as descendants (where we allow a node to be a
        descendant of itself).
        For a BST like this:
                                            6
                                         2     8
                                       0   4 7   9
        The lowest common ancestor node of p(2) and q(8) is 6 since 2 and 8 are both the
        descendant node of 6. What if p is 2 and q is 4? In this case, the LCA is 2 since
        a node can be a descendant of itself.
        Noted that the key characteristic of a binary search tree is the ordering of its
        elements. Each node in the tree has a value (or key), and the values in the left
        subtree of any node  are less than or equal to the value of that node, while the
        values in the right subtree are greater than or equal to the node's value.
        Now we understand the problem, we can start solving it. We can create a dummy node
        to replace the root node to make it more clear. Next, we using a while loop to
        iterate through the whole tree. Inside the while loop, we first check if the value
        of p and q are greater than the current root node. If it is, that means the LCA is
        definitely not gonna appear in the left subtree so we move the root node to the
        right subtree. Otherwise, we move the root to the left subtree. What if p and q is
        not both greater or lower than the root node? This is our exit condition, and we just
        return the current root node because it must be the LCA we are looking for.
        """

        cur = root

        while cur:
            if p.val > cur.val and q.val > cur.val:
                cur = cur.right
            elif p.val < cur.val and q.val < cur.val:
                cur = cur.left
            else:
                return cur


if __name__ == "__main__":
    sol = Solution()
    root = TreeNode(6)
    root.left = TreeNode(2)
    root.right = TreeNode(8)
    root.left.left = TreeNode(0)
    root.left.right = TreeNode(4)
    root.left.right.left = TreeNode(3)
    root.left.right.right = TreeNode(5)
    root.right.left = TreeNode(7)
    root.right.right = TreeNode(9)

    print(sol.lowestCommonAncestor(root, root.left.left, root.right.left).val)