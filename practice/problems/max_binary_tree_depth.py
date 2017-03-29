"""

https://leetcode.com/problems/maximum-depth-of-binary-tree/#/description


Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def traversePreOrder(self, root, path_len):
        if not root:
            return path_len

        path_len += 1
        left_len = self.traversePreOrder(root.left, path_len)
        right_len = self.traversePreOrder(root.right, path_len)

        if left_len > right_len:
            return left_len
        else:
            return right_len

    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        max_len = self.traversePreOrder(root, 0)

        return max_len