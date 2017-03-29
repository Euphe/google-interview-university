"""
http://interactivepython.org/runestone/static/pythonds/SortSearch/TheQuickSort.html
"""
def quick_sort(alist):
	_quick_sort(alist, 0, len(alist)-1)
	return alist

def _quick_sort(alist, first, last):
	print('quicksorting alist', alist[first:last+1])
	print('first', first, 'last', last)
	if first<last:

		pivot_index = first

		#find split point
		i = pivot_index+1
		j = last

		pivot = alist[pivot_index]
		print('pivot', pivot)
		while i < j:
			print('i',i,'j',j)
			left_mark = alist[i]
			right_mark = alist[j]

			#move left mark until left_mark > pivot
			while (i<=j and left_mark < pivot):
				i+=1
				left_mark = alist[i]

			#move right mark until right_mark < pivot
			while (i<=j and right_mark > pivot):
				j-=1
				right_mark = alist[j]

			if i < j:
				temp = alist[i]
				alist[i] = alist[j]
				alist[j] = temp
		split_index = j

		temp = alist[split_index]
		alist[split_index] = pivot
		alist[pivot_index] = temp

		_quick_sort(alist, first, split_index-1)
		_quick_sort(alist, split_index+1, last)

alist = [54,26,93,17,77,31,44,55,20]
quick_sort(alist)
print(alist)