"""
The basic operations we will implement for our binary heap are as follows:

MinHeap() creates a new, empty, binary heap.
put(k) adds a new item to the heap.
find_min() returns the item with the minimum key value, leaving item in the heap.
del_min() returns the item with the minimum key value, removing the item from the heap.
is_empty() returns true if the heap is empty, false otherwise.
__len__() returns the number of items in the heap.
_from_list(list) builds a new heap from a list of keys.

"""

class MinHeap:
	#Heap order: given node x, parent p, x >= p

	def __init__(self):
		self._list = []

	def put(self, x):
		#First append the item to the list
		index = len(self._list)
		self._list.append(x)

		#Then swap item with parent until the heap order property is valid
		while index//2 > 0:
			parent = self._list[int(index/2)]
			if self._list[index] < parent:
				#swap
				temp = self._list[int(index/2)]
				self._list[int(index/2)] = self._list[index]
				self._list[index] = temp
			
			else:
				break
			index = int(index/2)

	def find_min(self):
		if len(self._list) > 1:
			return self._list[1]

	def min_child(self, i):
		if i*2+1 > len(self._list)-1:
			return i*2
		else:
			if self._list[i*2+1] > self._list[i*2]:
				return i*2
			else:
				return i*2+1

	def del_min(self):
		
		if len(self._list) > 1:
			root = self._list[1] #Get the root of the tree
			#Put the last element of the tree in root's place
			self._list[1] = self._list[-1]
			del self._list[-1]
			#Swap the root with the smallest children until the heap order property is valid
			index = 1
			while index * 2 < len(self._list):
				
				min_child = self.min_child(index)

				if self._list[index] > self._list[min_child]:
					temp = self._list[min_child]
					self._list[min_child] = self._list[index]
					self._list[index] = temp
					index = min_child
				else:
					break

			return root

	def is_empty(self):
		return len(self) == 0

	def __len__(self):
		return len(self._list) - 1

	def _from_list(self, alist):
		
		self._list = [0] + alist[:]

		i = len(alist) // 2 #start in the middle of the list
		while (i > 0):
			#push the ith element as far down as it can go
			index = i
			while index * 2 < len(self._list):
				min_child = self.min_child(index)

				if self._list[index] > self._list[min_child]:
					temp = self._list[min_child]
					self._list[min_child] = self._list[index]
					self._list[index] = temp
					index = min_child
				else:
					break

			i = i - 1

min_heap = MinHeap()

test_nums = [0,5,9,11,14,18,19,21,33,17,27]
for num in test_nums:
	min_heap.put(num)
print(min_heap._list)
