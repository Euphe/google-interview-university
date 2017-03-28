class BinaryTree:
	def __init__(self, cargo, left_child=None, right_child=None):
		self.cargo = cargo
		self.left_child = left_child
		self.right_child = right_child

	def insert_left(self, cargo):
		node = BinaryTree(cargo)
		if self.left_child == None:
			self.left_child = node
		else:
			node.left_child = self.left_child
			self.left_child = node

	def insert_right(self, cargo):
		node = BinaryTree(cargo)

		if self.right_child == None:
			self.right_child = node
		else:
			node.right_child = self.right_child
			self.right_child = node

	def __repr__(self):
		out = '<node {}, left_child: {}, right_child: {}>'.format(self.cargo, self.left_child.cargo if self.left_child else 'None', self.right_child.cargo if self.right_child else 'None')
		return out