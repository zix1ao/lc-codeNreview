"""
An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.
You are also given three integers sr, sc, and color.
You should perform a flood fill on the image starting from the pixel image[sr][sc].
To perform a flood fill, consider the starting pixel,
plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel,
plus any pixels connected 4-directionally to those pixels (also with the same color), and so on.
Replace the color of all the aforementioned pixels with color.

Return the modified image after performing the flood fill.

Example 1:
Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]
Explanation: From the center of the image with position (sr, sc) = (1, 1) (i.e., the red pixel),
all pixels connected by a path of the same color as the starting pixel (i.e., the blue pixels) are colored with the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally connected to the starting pixel.

Example 2:
Input: image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, color = 0
Output: [[0,0,0],[0,0,0]]
Explanation: The starting pixel is already colored 0, so no changes are made to the image.

Constraints:
  ·m == image.length
  ·n == image[i].length
  ·1 <= m, n <= 50
  ·0 <= image[i][j], color < 216
  ·0 <= sr < m
  ·0 <= sc < n
"""

class Solution:
    def floodFill(self, image: [[int]], sr: int, sc: int, color: int) -> [[int]]:
        """
        :param image: [[int]
        :param sr: int
        :param sc: int
        :param color: int
        :return: [[int]]
        """

        """
        This problem is quite tricky at first glance. We are given a (m x n) integer
        grid image where image[i][j] represents the pixel value of the image. And we
        are also given three integers sr, sc and color. We should perform a flood fill
        on the image starting from the pixel image[sr][sc].
        To perform a flood fill, we should consider the starting pixel, plus any pixels
        connected 4-directionally to the starting pixel of the same color as the starting
        pixel, plus any pixels connected 4-directionally to those pixels
        (also with the same color), and so on. 
        We have to replace the color of all of the aforementioned pixels with "color".
        
        First of all, we will start checking at location(sr, sc) so we assign it to a
        variable called "current". Suppose the "color" is 1, we have to determine if
        "current" is equal to "color". If it is, then the starting pixel is already
        colored with the target color, so no changes need to be made and we return the
        original image. Otherwise, we will define an inner function called "fill", which
        take in the parameters: image, sr, sc, current, color. Inside this function, we
        have to check first if the starting coordinate is out of bounds or the current
        color is not the same as our parameter. Next, we will assign the current color
        to the new color. At this point, the problem is pretty straightforward. We just
        have to recursively call our fill function and change the coordinate to the up,
        down, left and right, with other parameters remain the same.
        """

        current = image[sr][sc]

        if current == color:
            return image

        self.fill(image, sr, sc, current, color)

        return image

    def fill(self, image, sr, sc, color, newColor):
        if sr < 0 or sc < 0 or sr >= len(image[0]) or sc >= len(image) or image[sr][sc] != color:
            return

        image[sr][sc] = newColor

        self.fill(image, sr - 1, sc, color, newColor)
        self.fill(image, sr + 1, sc, color, newColor)
        self.fill(image, sr, sc - 1, color, newColor)
        self.fill(image, sr, sc + 1, color, newColor)


if __name__ == "__main__":
    sol = Solution()
    print(sol.floodFill([[1,1,1],
                                [1,1,0],
                                [1,0,1]], 1, 1, 2))