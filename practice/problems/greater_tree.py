"""
https://leetcode.com/problems/convert-bst-to-greater-tree/#/description

Given a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus sum of all keys greater than the original key in BST.

Example:

Input: The root of a Binary Search Tree like this:
              5
            /   \
           2     13

Output: The root of a Greater Tree like this:
             18
            /   \
          20     13

"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
    	return "TreeNode = {}".format(self.val)

def list_to_btree(alist):
	root = None
	nodes = {}
	for i in range(len(alist)):
		if type(alist[i]) == int:
			node = TreeNode(alist[i])
		else:
			node = None
		nodes[i] = node

		if i == 0:
			root = node
		elif i == 1:
			root.left = node
		elif i == 2:
			root.right = node
		else:
			if i % 2 != 0: #odd
				parent_index = i//2

				nodes[parent_index].left = node
			else:
				parent_index = i//2 - 1
				nodes[parent_index].right = node

	return root







def _porder_sum(node, parent_value):
	#if there are right children - increase self value by their _porder_sum
	node.val += parent_value
	if node.right:
		node.val += _porder_sum(node.right, parent_value)-parent_value
	#if there are left children - increase their value by your value
	if node.left:
		_porder_sum(node.left, node.val)
	return node.val

def porder_sum(root):


	return root

class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        
        if not root:
            return None
            
        #postorder traversal
        new_root = porder_sum(root)
        return new_root

solution = Solution()
alist = [5,2,13, 1, 3]
tree = list_to_btree(alist)
new_tree = solution.convertBST(tree)