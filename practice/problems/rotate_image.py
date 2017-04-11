"""
https://leetcode.com/problems/rotate-image/#/description

You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Follow up:
Could you do this in-place?
"""
def transpose(m):
    for i in range(len(m)):
        for j in range(i, len(m)):
            temp = m[i][j]
            m[i][j] = m[j][i]
            m[j][i] = temp

def rotate_inplace(m):
    N = len(m)
    transpose(m)

    #reverse each row
    for i, al in enumerate(m):
        m[i] = m[i][::-1]

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """

        rotate_inplace(matrix)
            