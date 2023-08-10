"""
Given an array of meeting time intervals where intervals[i] = [start_i, end_i],
determine if a person could attend all meetings.

Example 1:
Input: intervals = [[0, 30],[5, 10],[15, 20]]
Output: false
Explanation: The first two meetings overlap, so a person cannot attend both.

Example 2:
Input: intervals = [[7,10],[2,4]]
Output: true

Constraints:
  ·0 <= intervals.length <= 10^4
  ·intervals[i][0] <= intervals[i][1]

"""


class Solution:
    def canAttendMeetings(self, intervals: [[int]]) -> bool:
        intervals.sort(key=lambda x: x[0])

        for i in range(1, len(intervals)):
            if intervals[i][0] < intervals[i - 1][1]:
                return False

        return True


if __name__ == '__main__':
    s = Solution()
    print(s.canAttendMeetings([[0, 30],[5, 10],[15, 20]]))
