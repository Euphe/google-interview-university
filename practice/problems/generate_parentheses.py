"""
https://leetcode.com/problems/generate-parentheses/#/description

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]

"""

def possible_parentheses(n, cur_text='(', open_par = 1, pairs = 0):

	if len(cur_text) == n*2:
		return [cur_text]

	combinations = []
	print('Cur text, open par, pairs', cur_text, open_par, pairs)
	if 2*n-len(cur_text) > open_par: #we can open a new pair
		print('Can open a new pair')
		combinations += possible_parentheses(n, cur_text+'(', open_par+1, pairs)
	print('Combinations with open par', combinations)
	if open_par > 0: #we can close a pair
		print('Can close a pair')
		combinations += possible_parentheses(n, cur_text+')', open_par-1, pairs+1)
	return combinations

print(possible_parentheses(3))