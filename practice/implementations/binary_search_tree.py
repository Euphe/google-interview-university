"""
http://interactivepython.org/runestone/static/pythonds/Trees/SearchTreeImplementation.html

BST() Create a new, empty map.
put(key,val) Add a new key-value pair to the map. If the key is already in the map then replace the old value with the new value.
get(key) Given a key, return the value stored in the map or None otherwise.
del Delete the key-value pair from the map using a statement of the form del map[key].
len() Return the number of key-value pairs stored in the map.
in Return True for a statement of the form key in map, if the given key is in the map.

"""

import random
class TreeNode:
	def __init__(self, key=None, cargo=None, parent=None, left_child=None, right_child=None):
		self.key = key
		self.cargo = cargo
		self.parent = parent
		self.left_child = left_child
		self.right_child = right_child

	def __repr__(self):
		return "<bst_node {} (p:{}, l:{}, r:{})".format(self.key, self.parent.key if self.parent else None, self.left_child.key if self.left_child else None, self.right_child.key if self.right_child else None, )

	def printout(self):
		print(self)
		if self.left_child:
			self.left_child.printout()		
		if self.right_child:
			self.right_child.printout()

		

class BinarySearchTree:
	#Order property: for value x, all values left of x are less than x, all values right of x are more than x
	def __init__(self):
		self.root = None
		self.size = 0

	def __len__(self):
		return self.size

	def __setitem__(self, key, value):
		return self.put(key, value)

	def __getitem__(self, key):
		return self.get(key)

	def __contains__(self, key):
		return bool(self.get(key))

	def find_min(self, node):
		while node:
			if not node.left_child:
				break
			node = node.left_child
		return node

	def find_successor(self, node):
		successor = None

		if node.right_child:
			successor = self.find_min(node.right_child)
		else:
			if node.parent:
				if node.parent.left_child == node:
					successor = node.parent
				else:
					node.parent.right_child = None
					successor = self.find_successor(node.parent)
					node.parent.right_child = node
		return successor

	def splice_node(self, node):
		if node.parent:
			is_left_child = False
			if node.parent.left_child == node:
				is_left_child  = True

		#If has no children
		if not node.left_child and not node.right_child:
			if not node.parent:
				self.root = None
				return 

			if is_left_child:
				node.parent.left_child  = None
			else:
				node.parent.right_child  = None
		elif node.left_child and not node.right_child or node.right_child and not node.left_child:
			#elif has 1 child
			child = node.left_child or node.right_child

			if not node.parent:
				#is root
				node.key = child.key
				node.cargo = child.cargo
				node.left_child = child.left_child #if node.left_child != child else child.left_child
				node.right_child = child.right_child #if node.left_child != child else child.right_child
				return 

			if is_left_child:
				node.parent.left_child = child
			else:
				node.parent.right_child = child
			child.parent = node.parent

	def __delitem__(self, key):
		return self.delete(key)

	def delete(self, key):
		node = self._get(key)
		if node:
			if node.left_child and node.right_child:
				#has 2 children
				successor = self.find_successor(node) #Get successor
				self.splice_node(successor) #Delete successor from tree
				node.key = successor.key #Replace current node with successor
				node.cargo = successor.cargo
			else:
				self.splice_node(node)
				

		else:
			raise(KeyError('Key not found in tree.'))

	def _get(self, key):
		current_node = self.root
		while current_node != None:
			if current_node.key == key:
				return current_node
			elif key < current_node.key:
				#move left
				current_node = current_node.left_child
			else:
				#move right
				current_node = current_node.right_child

		return None #search failed

	def get(self, key):
		search_result = self._get(key)
		if search_result != None:
			return search_result.cargo

	def _put(self, root, key, value):
		if root.key == key:
			root.cargo = value
		elif key < root.key:
			#move left
			if root.left_child:
				return self._put(root.left_child, key, value)
			else:
				#put the node here
				root.left_child = TreeNode(key, value, root)
				self.size+=1
		elif key > root.key:
			#move right
			if root.right_child:
				return self._put(root.right_child, key, value)
			else:
				#put the node here
				root.right_child = TreeNode(key, value, root)
				self.size+=1

	def put(self, key, value):
		node = TreeNode(key, value)
		if not self.root:
			self.root = node
		else:
			#recursively put
			self._put(self.root, key, value)

	def printout(self):
		if self.root:
			self.root.printout()



bst = BinarySearchTree()

test_numbers = [70,31,93,94,14,23,73]

for num in test_numbers:
	bst.put(num, num)

bst.printout()
bst.delete(70)
print('deld 70')
bst.printout()
