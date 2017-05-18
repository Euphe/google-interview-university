"""
Given a sequence of matrices, find the most efficient way to multiply these matrices together. The problem is not actually to perform the multiplications, but merely to decide in which order to perform the multiplications.

Given an array p[] which represents the chain of matrices such that the ith matrix Ai is of dimension p[i-1] x p[i]. We need to write a function MatrixChainOrder() that should return the minimum number of multiplications needed to multiply the chain.

Input: p[] = {40, 20, 30, 10, 30}   
Output: 26000  
There are 4 matrices of dimensions 40x20, 20x30, 30x10 and 10x30.
Let the input 4 matrices be A, B, C and D.  The minimum number of 
multiplications are obtained by putting parenthesis in following way
(A(BC))D --> 20*30*10 + 40*20*10 + 40*10*30

Input: p[] = {10, 20, 30, 40, 30} 
Output: 30000 
There are 4 matrices of dimensions 10x20, 20x30, 30x40 and 40x30. 
Let the input 4 matrices be A, B, C and D.  The minimum number of 
multiplications are obtained by putting parenthesis in following way
((AB)C)D --> 10*20*30 + 10*30*40 + 10*40*30

Input: p[] = {10, 20, 30}  
Output: 6000  
There are only two matrices of dimensions 10x20 and 20x30. So there 
is only one way to multiply the matrices, cost of which is 10*20*30
"""

INP = [10, 20, 30, 40,]

def mult_operations(dimensions1, dimensions2):
	return dimensions1[0] * dimensions1[1] * dimensions2[1]

def mult_result_dimensions(dimensions1, dimensions2):
	return (dimensions1[0], dimensions2[1])

def m_result(matrix1, matrix2):
	return mult_operations(matrix1, matrix2), mult_result_dimensions(matrix1, matrix2)

assert(mult_operations([10,20], [20,30])==10*20*30)
assert(mult_result_dimensions([10,20], [20,30])==(10,30))

def _best_mult(matrices):
	#print('seeking best in', matrices)
	if len(matrices) < 2:
		return (0, matrices[0])
	if len(matrices) == 2:
		#print('just two matrices, they are the best mult')
		return m_result(matrices[0], matrices[1])

	else:
		#first case, multiply 0th by 1st and then by the best possible mult of what's left
		#print('Trying first case: {} x {} x best right'.format(matrices[0], matrices[1]))
		a_x_b = m_result(matrices[0], matrices[1])
		a_x_b_operations = a_x_b[0]
		a_x_b_result = a_x_b[1]
		#print('Result:', a_x_b)
		#print('Seeking best right mult:')
		best_right_mult = _best_mult(matrices[2:])
		#print('Best right mult:', best_right_mult)
		best_right_mult_operations = best_right_mult[0]
		best_right_mult_result = best_right_mult[1]
		#print('Mult a_x_b by best right mult result:')
		a_x_b_x_rest = m_result(a_x_b_result, best_right_mult_result)
		#print(a_x_b_x_rest)
		a_x_b_x_rest_operations = a_x_b_x_rest[0]
		a_x_b_x_rest_result = a_x_b_x_rest[1]
		first_case = (a_x_b_operations+a_x_b_x_rest_operations+best_right_mult_operations, a_x_b_x_rest_result)
		#print('Total first case operations {}, total first case result {}'.format(first_case[0], first_case[1]))

		#second case, multiply 0oth by the best possible mult of all others
		#print('Trying second case {} by best right mult: '.format(matrices[0]))
		#print('Seeking best right mult:')
		best_right_mult = _best_mult(matrices[1:])
		#print('Best right mult:', best_right_mult)
		best_right_mult_operations = best_right_mult[0]
		best_right_mult_result = best_right_mult[1]
		a_x_rest = m_result(matrices[0], best_right_mult_result)
		#print('Mult {} by best right mult result: {}'.format(matrices[0], a_x_rest))
		a_x_rest_operations = a_x_rest[0]
		a_x_rest_result = a_x_rest[1]
		second_case = (a_x_rest_operations+best_right_mult_operations, a_x_rest_result)
		#print('Total second case operations {}, total second case result {}'.format(second_case[0], second_case[1]))

		#third case - same as first, but approach from far right
		#print('Trying third case: best left x {} x {}'.format(matrices[-2], matrices[-1]))
		a_x_b = m_result(matrices[-2], matrices[-1])
		a_x_b_operations = a_x_b[0]
		a_x_b_result = a_x_b[1]
		#print('-2th by -1th Result:', a_x_b)
		#print('Seeking best left mult:')
		best_left_mult = _best_mult(matrices[:-2])
		#print('Best left mult:', best_left_mult)
		best_left_mult_operations = best_left_mult[0]
		best_left_mult_result = best_left_mult[1]
		#print('Mult best left mult by a_x_b result:')
		rest_x_a_x_b = m_result(best_left_mult_result, a_x_b_result)
		#print(rest_x_a_x_b)
		rest_x_a_x_b_operations = rest_x_a_x_b[0]
		rest_x_a_x_b_result = rest_x_a_x_b[1]
		third_case = (a_x_b_operations+rest_x_a_x_b_operations+best_left_mult_operations, rest_x_a_x_b_result)
		#print('Total third case operations {}, total third case result {}'.format(third_case[0], third_case[1]))

		#fourth case - same as second, but approach from far right
		#print('Trying fourth case  best left mult by {}: '.format(matrices[-1]))
		#print('Seeking best left mult:')
		best_left_mult = _best_mult(matrices[:-1])
		#print('Best left mult:', best_left_mult)
		best_left_mult_operations = best_left_mult[0]
		best_left_mult_result = best_left_mult[1]
		rest_x_a = m_result(best_left_mult_result, matrices[-1])
		#print('Mult best left mult by {} result: {}'.format(matrices[-1], rest_x_a))
		rest_x_a_operations = rest_x_a[0]
		rest_x_a_result = rest_x_a[1]
		fourth_case = (rest_x_a_operations+best_left_mult_operations, rest_x_a_result)
		#print('Total fourth case operations {}, total fourth case result {}'.format(fourth_case[0], fourth_case[1]))

		return min( (first_case, second_case, third_case, fourth_case),key=lambda mult_result: mult_result[0])

def best_multiplication(dimensions):
	matrices = []
	for i in range(1, len(dimensions)):
		matrices.append((dimensions[i-1], dimensions[i]))

	return _best_mult(matrices)

def matrix_chain_order(matrix_dimensions):
	
	pass

print('Answer', best_multiplication(INP)[0])