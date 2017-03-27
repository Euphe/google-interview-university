"""
http://openbookproject.net/thinkcs/python/english3e/linked_lists.html

"""

class Node:
	def __init__(self, cargo=None, next_node=None):
		self.cargo = cargo
		self.next_node = next_node
	def __str__(self):
		out = str(self.cargo) + '---->'
		if self.next_node:
			out +=  str(self.next_node.cargo)
		return out 

class LinkedList:
	def __init__(self):
		self.length = 0 #invariant
		self.head = None

	def get_node(self, index):
		i = 0
		node = self.head
		while i < index:
			if node:
				node = node.next_node
			else:
				raise(ValueError('Index out of linked list bounds'))
			i+=1
		return node

	def get(self, index=0):
		if index < 0:
			raise(ValueError('Negative indicies not supported'))
		if index > self.length-1:
			raise(ValueError('Index out of linked list bounds'))
		node = self.get_node(index)
		if node:
			return node.cargo
		return None

	def insert(self, cargo, index=0):
		if index < 0:
			raise(ValueError('Negative indicies not supported'))
		if index > self.length:
			raise(ValueError('Index out of linked list bounds'))
		insert_node = Node(cargo)

		prev_node = None
		node = self.head

		for i in range(index):
			if node.next_node:
				prev_node = node
				node = node.next_node
			else:
				prev_node = node
				node = None
				break
				
		temp = node
		insert_node.next_node = node
		if prev_node:
			prev_node.next_node = insert_node
		if index == 0:
			self.head = insert_node

		self.length += 1

	def pop(self, index=0):
		if index < 0:
			raise(ValueError('Negative indicies not supported'))
		if index > self.length-1:
			raise(ValueError('Index out of linked list bounds'))

		prev_node = None
		node = self.head

		for i in range(index):
			if node.next_node:
				prev_node = node
				node = node.next_node
			else:
				raise(ValueError('Index out of linked list bounds'))

		if index == 0:
			self.head = node.next_node
		else:
			prev_node.next_node = node.next_node

		self.length -= 1
		return node.cargo

	def print_list(self):
		node = self.head
		for i in range(self.length):
			print(node)
			if node:
				node = node.next_node

	def get_list(self):
		items = []
		node = self.head
		while node:
			items.append(node.cargo)
			if node:
				node = node.next_node
		return items

#Tests
#creating
linked_list = LinkedList()

#Adding values to head
values = [1, 2, 3]
for val in values:
	linked_list.insert(val)

linked_list.print_list()
print(linked_list.get_list())
assert(linked_list.get_list() == [3, 2, 1])
assert(linked_list.length == 3)

#Popping from head
assert(linked_list.pop() == 3 and linked_list.get_list() == [2, 1])
assert(linked_list.length == 2)
linked_list.print_list()

#Inserting to middle
print("inserting 4 to index 1")
print(linked_list.get_list())
linked_list.insert(4,1)
assert(linked_list.length == 3)
linked_list.print_list()
print(linked_list.get_list())

#Inserting to end
print("inserting 4 to index 3")
print(linked_list.get_list())
linked_list.insert(4,3)
assert(linked_list.length == 4)
linked_list.print_list()
print(linked_list.get_list())

#Inserting past end
print("inserting 4 to index 5")
print(linked_list.get_list())
excepted = False
try:
	linked_list.insert(4,5)
except ValueError as e:
	excepted = True
	assert(str(e) == 'Index out of linked list bounds')
finally:
	assert(excepted)
	assert(linked_list.length == 4)
linked_list.print_list()
print(linked_list.get_list())

#Inserting to -1
print("inserting 6 to index -1")
print(linked_list.get_list())
excepted = False
try:
	linked_list.insert(4,-1)
except ValueError as e:
	excepted = True
	assert(str(e) == 'Negative indicies not supported')
finally:
	linked_list.print_list()
	print(linked_list.get_list())
	assert(excepted)
	assert(linked_list.length == 4)



#Popping from past end
print("Popping from index 4")
print(linked_list.get_list())
excepted = False
try:
	linked_list.pop(4)
except ValueError as e:
	excepted = True
	assert(str(e) == 'Index out of linked list bounds')
finally:
	linked_list.print_list()
	print(linked_list.get_list())
	assert(excepted)
	assert(linked_list.length == 4)

#Popping from end
print("Popping from index 3")
print(linked_list.get_list())
excepted = False
popped = linked_list.pop(3)
assert(popped == 4 and linked_list.get_list() == [2,4,1])
assert(linked_list.length == 3)

#Getting from end
print("Getting from index 2")
print(linked_list.get_list())

get = linked_list.get(2)
assert(get == 1)
print('got:', get)


#Getting from past end
print("Getting from index 3")
print(linked_list.get_list())
try:
	get = linked_list.get(3)
except ValueError as e:
	excepted = True
	assert(str(e) == 'Index out of linked list bounds')
finally:
	assert(excepted)

#Getting from -1
print("Getting from index -1")
print(linked_list.get_list())
try:
	get = linked_list.get(-1)
except ValueError as e:
	excepted = True
	assert(str(e) == 'Negative indicies not supported')
finally:
	assert(excepted)

#Getting from 1
print("Getting from index 1")
print(linked_list.get_list())
get = linked_list.get(1)
assert(get == 4)
print('got:', get)
