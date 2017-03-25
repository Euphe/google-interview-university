"""
http://openbookproject.net/thinkcs/python/english3e/linked_lists.html

"""

class Node:
	def __init__(self, cargo=None, next_node=None):
		self.cargo = cargo
		self.next_node = next_node
	def __str__(self):
		return str(self.cargo) + ' ----> ' + str(self.next_node.cargo) if self.next_node else ''

class LinkedList:
	def __init__(self):
		self.length = 0 #invariant
		self.head = None

	def get_node(self, index):
		i = 0
		node = self.head
		while i < index:
			print('iterating over nodes, i=', i)
			if node:
				node = node.next_node
			else:
				raise(ValueError('Index out of linked list bounds'))
			i+=1
		return node

	def get(self, index=0):
		node = self.get_node(index)
		if node:
			return node.cargo
		return None

	def insert(self, cargo, index=0):
		node = Node(cargo)
		print('inserting', cargo)
		if not self.head:
			self.head = node
			self.length += 1
			return 

		prevNode = self.head
		for i in range(index):
			if prevNode.next_node:
				prevNode = prevNode.next_node
			else:
				break

		if prevNode:
			temp = prevNode.next_node
			node.next_node = temp
			prevNode.next_node = node
			self.length += 1

	def pop(self, index):
		prevNode = self.get_node(index-1)
		node = self.get_node(index)
		prevNode.next = node.next

		self.length -= 1
		return node.cargo

#Tests
#creating
linked_list = LinkedList()

#Adding values
values = [1, 2, 3]
for val in values:
	linked_list.insert(val)


for i in range(linked_list.length):
	print(linked_list.get(i))
