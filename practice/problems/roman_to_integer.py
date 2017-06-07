"""
https://leetcode.com/problems/roman-to-integer/#/description

Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.

"""

class Solution(object):

    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        ROMAN_NUMBERS = {
        	"I": 1,
        	"V": 5,
        	"X": 10,
        	"L": 50,
        	"M": 1000,
        	"D": 500,
        	"C": 100
        }

        ROMAN_SUBSTRACTION_NOTATION = {
        	"IV": 4,
        	"IX": 9,
        	"XL": 40,
        	"XC": 90,
        	"CD": 400,
        	"CM": 900
        }

        parsed_numbers = []
        parsed_str = list(s)
        #first scan string for substraction
        i = 0
        while i < len(parsed_str)-1:
        	numeral_pair = parsed_str[i] + parsed_str[i+1]
        	if numeral_pair in ROMAN_SUBSTRACTION_NOTATION:
        		parsed_numbers.append(ROMAN_SUBSTRACTION_NOTATION[numeral_pair])
        		del parsed_str[i+1]
        		del parsed_str[i]
        		continue
        	i+=1
        #then scan for individual numbers
        for numeral in parsed_str:
        	parsed_numbers.append(ROMAN_NUMBERS[numeral])

        
        return sum(parsed_numbers)


solution = Solution()

data = "MCMXCVI"

print(solution.romanToInt(data))

#The solution was accepted, but its not entirely correct
#For example it fails for "wrongly written roman numerals", such as IXL