"""

https://leetcode.com/problems/find-bottom-left-tree-value/#/description


Given a binary tree, find the leftmost value in the last row of the tree.

Example 1:
Input:

    2
   / \
  1   3

Output:
1
Example 2: 
Input:

        1
       / \
      2   3
     /   / \
    4   5   6
       /
      7

Output:
7

"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def find_fartherest_left(self, root, path_len, far_node_val):
        if not root:
            # print('nil node, returning', path_len, far_node_val)
            return path_len, far_node_val
        path_len+=1
        # print('proper node ', root.val,' path_len is now', path_len)
        if root.left:
            far_node_val = root.left.val
        elif root.right:
            far_node_val = root.right.val
            # print('node had left child, farest node is now ', far_node_val)
        
        # print('In node ', root.val, 'Traversing left and right',)
        left_path, left_nodeval = self.find_fartherest_left(root.left, path_len, far_node_val)
        right_path, right_nodeval = self.find_fartherest_left(root.right, path_len, far_node_val)
        # print('In node ', root.val, 'Received from left and right:')
        # print('On the left:', left_path, left_nodeval)
        # print('On the right:', right_path, right_nodeval)
        
        max_path = path_len
        
        if left_path > path_len and left_path >= right_path:
            max_path = left_path
            far_node_val = left_nodeval
        elif right_path > path_len and right_path > left_path:
            max_path = right_path
            far_node_val = right_nodeval
        else:
            max_path=  path_len
        return max_path, far_node_val

    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        pathlen, nodeval = self.find_fartherest_left(root, 0, root.val)

        return nodeval