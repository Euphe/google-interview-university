"""
http://interactivepython.org/runestone/static/pythonds/SortSearch/TheMergeSort.html

"""

def merge(out, al1, al2):
	#0 assuming both al1 and al2 are sorted 
	#1 choose the smallest element of two
	#2 remove it from its list
	#3 place the removed element in the output
	#4 repeat until one list is empty
	#5 once one list is empty just put the remaining list into the output 

	k=0
	i = 0
	j = 0
	while (i < len(al1)) and (j < len(al2)):
		if al1[i] <= al2[j]:
			out[k] = al1[i]
			i+=1
		else:
			out[k] = al2[j]
			j+=1
		k+=1

	while (i < len(al1)):
		out[k] = al1[i]
		k+=1
		i+=1

	while (j < len(al2)):
		out[k] = al2[j]
		k+=1
		j+=1
	return out


def merge_sort(alist):

	if len(alist) <= 1:
		return alist #its sorted
	print('merge sortin', alist)
	#split into two lists
	left_list = merge_sort(alist[len(alist)//2:])
	right_list = merge_sort(alist[:len(alist)//2])
	print('got left', left_list)
	print('got right', right_list)
	#merge
	#repeadetely get smallest item of both lists and put into original list
	alist = merge(alist, left_list, right_list)
	print('murged', alist)
	return alist