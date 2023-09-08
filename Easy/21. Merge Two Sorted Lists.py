"""
You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists into one sorted list.
The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: list1 = [], list2 = []
Output: []

Example 3:
Input: list1 = [], list2 = [0]
Output: [0]

Constraints:
  ·The number of nodes in both lists is in the range [0, 50].
  ·-100 <= Node.val <= 100
  ·Both list1 and list2 are sorted in non-decreasing order.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: [ListNode], list2: [ListNode]) -> [ListNode]:
        """
        :param list1: [ListNode]
        :param list2: [ListNode]
        :return: [ListNode]
        """

        """
        The problem is asking us to merge two sorted linked list into one
        and return the head of it.
        First we can create an empty listnode and its dummy listnode.
        Then we compare the value of two linked list while they are not
        empty and store the smaller one into that dummy listnode we created
        before and move the list pointer to the next position. After comparing,
        we move the dummmy listnode pointer to the next position. Finally, we
        shall consider some edge cases, where one of the linked list is already
        empty while the other is not. In this case, append that non-empty list
        to the next position of dummy listnode. 
        """

        current = mergedList = ListNode()

        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next

            current = current.next

        if list1:
            current.next = list1
        elif list2:
            current.next = list2

        return mergedList.next


def create_linked_list(values):
    head = ListNode()
    current = head
    for value in values:
        current.next = ListNode(value)
        current = current.next
    return head.next


if __name__ == '__main__':
    s = Solution()
    list1 = create_linked_list([1, 2, 4])
    list2 = create_linked_list([1, 3, 4])
    result = s.mergeTwoLists(list1, list2)

    merged_list = []
    while result:
        merged_list.append(result.val)
        result = result.next

    print(merged_list)