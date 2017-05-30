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

def get_operations(diff, cookies):
	operations = 0
	for i, c in enumerate(cookies):
		x = cookies[i]-diff
		while x > 0:
			operations+= x // 5
			x = x % 5

			operations+= x // 2
			x = x % 2

			operations+= x // 1
			x = x % 1
	return operations


def equalize(cookies):
	min_cookies = min(cookies)

	cookie_diff = [x-min_cookies for x in cookies]

	diffs = [min_cookies-i for i in range(5)]
	operations = [get_operations(diff, cookies) for diff in diffs]

	return min(operations)

t = int(input().strip())
for a0 in range(t):
    N = int(input().strip())
    cookies = list(map(int, input().strip().split(' ')))
    print(equalize(cookies))


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