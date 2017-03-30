"""
https://leetcode.com/problems/count-primes/#/description

Description:

Count the number of prime numbers less than a non-negative number, n.

A prime number (or a prime) is a natural number greater than 1 that has no positive divisors other than 1 and itself. 

"""

class Solution(object):
	def is_prime(self, n):
		#brute
		if n <= 1:
			return False

		for num in range(2, n):
			if n % num == 0:
				return False
		return True

    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
