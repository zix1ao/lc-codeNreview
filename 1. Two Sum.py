"""
Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution,
and you may not use the same element twice.

You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]

Constraints:
  ·2 <= nums.length <= 10^4
  ·-10^9 <= nums[i] <= 10^9
  ·-10^9 <= target <= 10^9
  ·Only one valid answer exists.
"""


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        # Brute Force Approach

        # result = []
        # for i in range(0, len(nums)):
        #     for j in range(0, len(nums)):
        #         if nums[i] + nums[j] == target and i != j:
        #             result.append(i)
        #             result.append(j)
        #             return result
            #     else:
            #         j += 1
            # i += 1

        # Hash Table

        # hash_table = {}
        # n = len(nums)
        #
        # for index, element in enumerate(nums):
        #     hash_table[element] = index

        # numMap = {}
        # n = len(nums)
        #
        # for i in range(n):
        #     numMap[nums[i]] = i

        # for i in range(n):
        #     complement = target - nums[i]
        #     if complement in hash_table and hash_table[complement] != i:
        #         return [i, hash_table[complement]]

        # for element in nums:
        #     complement = target - element
        #     if complement in hash_table:
        #         return [hash_table[element], hash_table[complement]]
        #     else:
        #         hash_table[element] = nums.index(element)

        """
        The problem is asking us to find two numbers in an array
        whose sum are equal to the target value.
        Firstly, we need to create a dictionary. Then we loop through
        the array and in each loop, we calculate the complement value
        by subtracting the current value from the target value and store
        it in a variable called result. Next, we check if the complement 
        value is in the dictionary. If it is, we return the index of the
        complement value and the current index. If it is not, we add the
        current value and its index to the dictionary.
        """


        # d = {}
        # for index in range(len(nums)):
        #     result = target - nums[index]
        #     print(d)
        #     if result in d:
        #         return [d[result], index]
        #     d[nums[index]] = index

        #     if complement := target - element in hash_table and hash_table[complement] != hash_table[element]:
        # return [hash_table[element], hash_table[complement]]


if __name__ == '__main__':
    nums = [1, 3, 2, 4, 8]
    target = 9
    # nums = [2, 7, 11, 15]
    # target = 9
    s = Solution()
    print(s.twoSum(nums, target))