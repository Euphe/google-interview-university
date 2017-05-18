"""
https://www.hackerrank.com/challenges/equal

Christy is interning at HackerRank. One day she has to distribute some chocolates to her colleagues. She is biased towards her friends and may have distributed the chocolates unequally. One of the program managers gets to know this and orders Christy to make sure everyone gets equal number of chocolates.

But to make things difficult for the intern, she is ordered to equalize the number of chocolates for every colleague in the following manner,

For every operation, she can choose one of her colleagues and can do one of the three things.

She can give one chocolate to every colleague other than chosen one.
She can give two chocolates to every colleague other than chosen one.
She can give five chocolates to every colleague other than chosen one.
Calculate minimum number of such operations needed to ensure that every colleague has the same number of chocolates. 

Input Format

First line contains an integer  denoting the number of testcases.  testcases follow. 
Each testcase has  lines. First line of each testcase contains an integer  denoting the number of colleagues. Second line contains N space separated integers denoting the current number of chocolates each colleague has.

Constraints



Number of initial chocolates each colleague has < 

Output Format

 lines, each containing the minimum number of operations needed to make sure all colleagues have the same number of chocolates.

Sample Input

1
4
2 2 3 7
Sample Output

2

"""
import sys
T = 1
cookies = [2, 2, 3, 7]

def operation(opernum, cookies, collegue):
	new_cookies = list(cookies)
	for i in range(len(cookies)):
		if i != collegue:
			if opernum == 1:
				new_cookies[i]+= 1
			elif opernum == 2:
				new_cookies[i]+= 2
			elif opernum == 3:
				new_cookies[i]+= 5
			else:
				raise(ValueError('Invalid operation'))
	return new_cookies

rec_level = 0
def equalize(cookies, collegue): #Returns the minimal amount of operations required to equalize all numbers in a sequence

	#if collegue invalid then its an impossible to apply any operations to him
	if collegue<0:
		return 999999999999999 

	#if no cookies are given then everyone is equal, communism!
	if not cookies:
		return 0

	#base case, check for equality
	if len(set(cookies))==1:
		return 0

	min_collegue = min(enumerate(cookies), key = lambda x: x[1])[0]
	if min_collegue == collegue:
		#There is no point in applying any operations to that collegue anymore
		return equalize(cookies, collegue-1)

	#Four cases:
		#Either we apply operation 1 to collegue
		#or we apply operation 2 to collegue
		#or we apply operation 3 to collegue
		#or we don't apply any operations to that collegue
	case1 = equalize(operation(1, cookies, collegue), collegue)+1
	case2 = equalize(operation(2, cookies, collegue), collegue)+1
	case3 = equalize(operation(3, cookies, collegue), collegue)+1
	case4 = equalize(cookies, collegue-1)

	return min([case1, case2, case3, case4])

#cookies = [1,2,4]
print('Answer', equalize(cookies, len(cookies)-1))


"""
Someone's solution from the interwebs

def minOpers(interns, target):
    count = 0
    for curr in interns:
        if curr - target >= 5:
            count += (curr - target) // 5
            curr = target + (curr - target) % 5
        if curr - target >= 2:
            count += (curr - target) // 2
            curr = target + (curr - target) % 2
        if curr - target == 1:
            count += 1
    return count

t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    interns = input().strip().split(' ')
    interns = sorted([int(i) for i in interns])
    target = interns[0]
    scores = [minOpers(interns, target)]
    if target >= 2:
        scores.append(minOpers(interns, target - 2))
    if target >= 1:
        scores.append(minOpers(interns, target - 1))
    print(min(scores))
"""