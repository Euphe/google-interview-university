"""
https://leetcode.com/problems/sqrtx/#/description

Implement int sqrt(int x).

Compute and return the square root of x.
"""
def binary_search(left, right, x):
	half = (right + left)//2
	if half < 1:
		return None

	if	half * half <= x < (half+1)*(half+1):
		return int(half)
	
	square = half * half
	if square > x:
		return binary_search(left, half, x)
	else:
		return binary_search(half, right, x)

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """

        if x == 0:
        	return 0

        if x < 0:
        	return None
        if x == 1:
        	return 1

        return binary_search(0, x, x)

solution = Solution()
print(solution.mySqrt(2))
print(solution.mySqrt(9))
print(solution.mySqrt(3))
print(solution.mySqrt(0))
print(solution.mySqrt(1))
print(solution.mySqrt(2147395599))