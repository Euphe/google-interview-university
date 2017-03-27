"""
implement hash table with array using linear probing
        - hash(k, m) - m is size of hash table
        - add(key, value) - if key already exists, update value
        - exists(key)
        - get(key)
        - remove(key)
"""
import better_exceptions
class HashTable:
	def __init__(self):
		self.size = 10
		self.keys = [None]*self.size
		self.data = [None]*self.size

	def hash_function(self, x):
		return x % self.size

	def put(self, key, value):

		hash_value = self.hash_function(key)

		if self.keys[hash_value] == None:
			self.data[hash_value] = value
			self.keys[hash_value] = key
			return
		

		#probing
		i = self.keys.index(self.keys[hash_value])
		initial_index = i
		while True:
			if i < self.size-1:
				if self.keys[i] == key:
					self.data[i] = value
					return
				if self.keys[i] == None or self.keys[i] == 'del':
					self.keys[i] = key
					self.data[i] = value
					return
			if i < self.size-1:
				i += 1
			else:
				i = 0
			if i == initial_index:
				break
		raise(RunTimeError('Hash table overflow'))

	def delete(self, key):
		
		hash_value = self.hash_function(key)

		if not self.keys[hash_value]:
			raise(KeyError(key))

		#probing
		i = self.keys.index(self.keys[hash_value])
		initial_index = i
		while True:
			if i < self.size-1:
				if self.keys[i] == key:
					self.data[i] = 'del'
					self.keys[i] = 'del'
					return 
				if self.keys[i] == None:
					raise(KeyError(key))

			if i < self.size-1:
				i += 1
			else:
				i = 0
			if i == initial_index:
				break


	def get(self, key):
		hash_value = self.hash_function(key)
		if self.keys[hash_value] == None:
			return None

		#probing
		i = self.keys.index(self.keys[hash_value])
		initial_index = i
		while True:
			if i < self.size-1:
				if self.keys[i] == key:
					return self.data[i]
				if self.keys[i] == None:
					return None
			if i < self.size-1:
				i += 1
			else:
				i = 0
			if i == initial_index:
				break
		return None


	def __getitem__(self, key):
		return self.get(key)

	def __setitem__(self, key, value):
		return self.put(key, value)

	def printout(self):
		print(self.keys)
		print(self.data)

table = HashTable()

table.put(1, 'data1')
table.printout()
table.put(1, 'data1.1')
table.printout()
table.put(11, 'data11')
table.printout()

table.put(75, 'data75')
table.printout()

print(table.get(1))
print(table.get(11))
print(table.get(75))

table[13] = 'data13'
table[33] = 'data33'
table.printout()
print(table[33])
print(table[13])
table[33] = 'data33.1'
print(table[33])
table[43] = 'data43.unreachable'
table.delete(33)
table.printout()
print(table[43])
