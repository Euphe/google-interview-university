#!/bin/python3
"""
https://www.hackerrank.com/challenges/stockmax

Your algorithms have become so good at predicting the market that you now know what the share price of Wooden Orange Toothpicks Inc. (WOT) will be for the next N days.

Each day, you can either buy one share of WOT, sell any number of shares of WOT that you own, or not make any transaction at all. What is the maximum profit you can obtain with an optimum trading strategy?

The first line contains the number of test cases T. T test cases follow:

The first line of each test case contains a number N. The next line contains N integers, denoting the predicted price of WOT shares for the next N days.


1 <= T <= 10

1 <= N <= 50000

share prices between 1 and 100000
Output Format

Output T lines, containing the maximum profit which can be obtained for the corresponding test case.



Sample Input

3
3
5 3 2
3
1 2 100
4
1 3 1 2
Sample Output

0
197
3

Explanation

For the first case, you cannot obtain any profit because the share price never rises. 
For the second case, you can buy one share on the first two days, and sell both of them on the third day. 
For the third case, you can buy one share on day 1, sell one on day 2, buy one share on day 3, and sell one share on day 4.
"""


import sys


# t = int(input().strip())
# for a0 in range(t):
#     N = int(input().strip())
#     prices = list(map(int, input().strip().split(' ')))

# 

prices = [1,3,1,2]
#prices = [0, 0, 1]
prices = [100 for i in range(50000)] + [100]
#prices = [1, 2]
#prices = [1, 0, 0, 0]
def stockmax_recursive_brute(shares, profit, prices): #returns maximum profit
	#base case: no more prices

	if not prices:
		return profit

	# print('Price is currently {}'.format(prices[0]))
	# print('Shares: {}, profit: {}'.format(shares, profit))
	# print('')

	case_buy = stockmax(shares+1, profit-prices[0], prices[1:])
	if shares > 0:
		case_sell = stockmax(0, profit+shares*prices[0], prices[1:])
	else:
		case_sell = 0
	case_skip = stockmax(shares, profit, prices[1:])

	return max(case_buy, case_sell, case_skip)

def stockmax_recursive_smart(prices):
	#find max price
	if len(prices) < 2:
		return 0

	max_price_ind = max(enumerate(prices), key= lambda x: x[1])[0]
	left_of_max = prices[:max_price_ind]
	max_price = prices[max_price_ind]

	profit = 0
	for price in left_of_max:
		profit -= price
		profit += max_price


	right_of_max= prices[max_price_ind+1:]

	return profit + stockmax_recursive_smart(right_of_max)

def stockmax_iterative(prices):
	if len(prices) < 2:
		return 0

	profit = 0

	l = 0
	r = len(prices)
	while l < r:
		max_price_ind = l+max(enumerate(prices[l:r]), key= lambda x: x[1])[0]
		max_price = prices[max_price_ind]
		for i in range(l, max_price_ind):
			profit-= prices[i]
			profit+= prices[i]*max_price
		l = max_price_ind+1
	return profit
print(stockmax_iterative(prices))