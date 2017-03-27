"""
http://openbookproject.net/thinkcs/python/english3e/queues.html

Write an implementation of the Priority Queue ADT using a linked list. 
You should keep the list sorted so that removal is a constant time operation. 


__init__
Initialize a new empty queue.

insert
Add a new item to the queue.
remove
Remove and return an item from the queue. The item that is returned is the one with the highest priority.

is_empty
Check whether the queue is empty.


Sort golfers by score in descending order
"""

class Golfer:
	def __init__(self, name, score):
		self.name = name
		self.score = score

	def __gt__(self, other):
		if type(other) != type(self):
			raise(TypeError("Can't compare {0} to {1}".format(type(self), type(other))))
		return self.score > other.score

	def __str__(self):
		return self.name + ': '+str(self.score)


class Node:
	def __init__(self, cargo=None, next_node=None):
		self.cargo = cargo
		self.next_node = next_node
	def __str__(self):
		out = str(self.cargo) + '---->'
		if self.next_node:
			out +=  str(self.next_node.cargo)
		return out 

	def __gt__(self, other):
		return self.cargo > other.cargo

class PriorityQueue:
	def __init__(self):
		self.head = None

	def insert(self, item):
		insert_node = Node(cargo=item)
		if not self.head:
			self.head = insert_node
			return 

		prev_node = None
		node = self.head
		while node:
			if insert_node > node:
				if prev_node:
					prev_node.next_node = insert_node
				insert_node.next_node = node

				if node == self.head:
					self.head = insert_node
				break
			prev_node = node
			node = node.next_node

			if not node.next_node:
				node.next_node = insert_node
				break

	def printout(self):
		node = self.head
		print('Printing queue')
		while node:
			print(node)
			node = node.next_node

	def pop(self):
		if self.head:
			item = self.head.cargo
			self.head = self.head.next_node
			return item

	def is_empty(self):
		if self.head:
			return False
		else:
			return True


golfer1 = Golfer('Mike Tyson', 10)
golfer2 = Golfer('Ivan Ivanovsky', 14)

queue = PriorityQueue()
queue.insert(golfer1)
queue.printout()
queue.insert(golfer2)
queue.printout()

queue.insert(Golfer('markov', 1))
queue.printout()

zegov = Golfer('zegov', 100)
queue.insert(zegov)
queue.printout()

queue.insert(Golfer('middlov', 12))
queue.printout()

assert(queue.pop() == zegov)
queue.printout()

assert(queue.is_empty() == False)
queue.pop()
queue.pop()
queue.pop()
queue.pop()
assert(queue.is_empty() == True)
queue.printout()