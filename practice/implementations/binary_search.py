"""
Implement binary search using recursion


"""
import random

array = sorted([random.randint(0, 1000) for i in range(1000)])

def binary_search(array, value):
	arrlen = len(array)
	if arrlen == 0:
		return False

	if arrlen == 1:
		if array[0] == value:
			return True
		else:
			return False

	middle = int(arrlen/2)
	middle_item = array[middle]

	if middle_item == value:
		return True
	if middle_item > value:
		return binary_search(array[:middle], value)
	else:
		return binary_search(array[middle+1:], value)


print(binary_search(array, 42))

print(binary_search([1, 2], 2))

print(binary_search([], 2))

print(binary_search([1, 2], 5))