"""
Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:
Input: head = [1,2]
Output: [2,1]

Example 3:
Input: head = []
Output: []

Constraints:
  ·The number of nodes in the list is the range [0, 5000].
  ·-5000 <= Node.val <= 5000
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: [ListNode]) -> [ListNode]:
        # Iterative Method

        prev = None

        while head:
            forward = head.next
            head.next = prev
            prev = head
            head = forward

        return prev

        # Recursive Method

        # if not head:
        #     return None
        #
        # newHead = head
        #
        # if head.next:
        #     newHead = self.reverseList(head.next)
        #     head.next.next = head
        #
        # head.next = None
        #
        # return newHead


if __name__ == "__main__":
    sol = Solution()
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    print(sol.reverseList(head))