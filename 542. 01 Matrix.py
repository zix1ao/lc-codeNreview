"""
Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.
The distance between two adjacent cells is 1.

Example 1:
Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
Output: [[0,0,0],[0,1,0],[0,0,0]]

Example 2:
Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
Output: [[0,0,0],[0,1,0],[1,2,1]]

Constraints:
  ·m == mat.length
  ·n == mat[i].length
  ·1 <= m, n <= 104
  ·1 <= m * n <= 104
  ·mat[i][j] is either 0 or 1.
  ·There is at least one 0 in mat.
"""
from collections import deque


class Solution:
    def updateMatrix(self, mat: [[int]]) -> [[int]]:
        rows, cols = len(mat), len(mat[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        queue = deque()

        result = [[float('inf')] * cols for _ in range(rows)]

        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    queue.append((r, c))
                    result[r][c] = 0

        while queue:
            curr_r, curr_c = queue.popleft()
            for dr, dc in directions:
                new_r, new_c = curr_r + dr, curr_c + dc
                if 0 <= new_r < rows and 0 <= new_c < cols and \
                        result[new_r][new_c] > result[curr_r][curr_c] + 1:
                    result[new_r][new_c] = result[curr_r][curr_c] + 1
                    queue.append((new_r, new_c))

        return result


if __name__ == "__main__":
    sol = Solution()
    print(sol.updateMatrix([[0, 0, 0], [0, 1, 0], [1, 1, 1]]))
