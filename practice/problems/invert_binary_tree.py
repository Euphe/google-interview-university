"""
https://leetcode.com/problems/invert-binary-tree/#/description

Invert a binary tree.

     4
   /   \
  2     7
 / \   / \
1   3 6   9
to
     4
   /   \
  7     2
 / \   / \
9   6 3   1


"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """ 
        if not root:
            return None

        root.left = self.invertTree(root.left)
        root.right = self.invertTree(root.right)
        temp = root.right
        root.right = root.left
        root.left = temp
        return root
        