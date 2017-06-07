"""
https://leetcode.com/problems/unique-paths/#/description

A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?

Note: m and n will be at most 100.

"""

def unique_paths(m, n):
	if m == 1 or n == 1:
		return 1
	dp = [[None for i in range(n)] for i in range(m)] #dp[i][j] is the amount of paths to cell i,j

	#base case, first column and first row are reachable by 1 path

	for i in range(m):
		dp[i][0] = 1
	for j in range(n):
		dp[0][j] = 1

	#fill the table, bottom up
	for i in range(1, m):
		for j in range(1, n):
			dp[i][j] = dp[i-1][j] + dp[i][j-1]

	return dp[-1][-1]