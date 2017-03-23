"""
https://leetcode.com/problems/number-complement/#/description

Given a positive integer, output its complement number. The complement strategy is to flip the bits of its binary representation.

Note:
The given integer is guaranteed to fit within the range of a 32-bit signed integer.
You could assume no leading zero bit in the integer’s binary representation.
Example 1:
Input: 5
Output: 2
Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010. So you need to output 2.
Example 2:
Input: 1
Output: 0
Explanation: The binary representation of 1 is 1 (no leading zero bits), and its complement is 0. So you need to output 0.
Subscribe to see which companies asked this question.
"""

class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        binary = "{0:b}".format(num)
        flipped = binary.replace('1', '2').replace('0', '1').replace('2','0')
        intform = 0

        for i, b in enumerate(flipped):
            if b != '0':
                intform += 2**(len(flipped)-i-1)
        
        return intform

solution = Solution()

assert(solution.findComplement(5)== 2)
assert(solution.findComplement(1)== 0)
assert(solution.findComplement(2)== 1)