"""
https://leetcode.com/problems/merge-two-binary-trees/#/description

Given two binary trees and imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not.

You need to merge them into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of new tree.

Example 1:
Input: 
	Tree 1                     Tree 2                  
          1                         2                             
         / \                       / \                            
        3   2                     1   3                        
       /                           \   \                      
      5                             4   7                  
Output: 
Merged tree:
	     3
	    / \
	   4   5
	  / \   \ 
	 5   4   7


"""

# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def process_nodes(t1, t2): # double inorder traversal
    if t1 and t2:
        t1.val += t2.val
    elif t2 and not t1:
        return t2
    elif t1 and not t2:
        return t1
    elif not t1 and not t2:
        return None
    
    t1.left = process_nodes(t1.left, t2.left)
    t1.right = process_nodes(t1.right, t2.right)
    return t1
    
        
class Solution:
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        
        t1 = process_nodes(t1, t2)
        return t1
        
        