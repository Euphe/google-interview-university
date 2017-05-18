"""
https://www.hackerrank.com/challenges/fibonacci-modified
We define a modified Fibonacci sequence using the following definition:
t(i+2) = t(i) + t(i+1)^2

Input Format

A single line of three space-separated integers describing the respective values of t1, t2, and n.

Constraints
3 <= n <= 20
tn may far exceed the range of a -bit integer.
Output Format

Print a single integer denoting the value of term  in the modified Fibonacci sequence where the first two terms are t1 and t2.
"""


def mfib(t1, t2, n):
	if n == 1:
		return t1
	if n == 2:
		return t2

	return mfib(t1, t2, n-2)+mfib(t1, t2, n-1)*mfib(t1, t2, n-1)

def mfib_dp(t1, t2, n):
	dp = [0 for i in range(n)]
	dp[0] = t1
	dp[1] = t2
	i = 0
	for i in range(2, n):
		dp[i] = dp[i-2] + dp[i-1]**2
	return dp[n-1]

print(mfib(0, 1, 20))
#print(mfib_dp(0, 1, 20))