"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows.
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".


Zigzag pattern:

/*n=numRows
Δ=2n-2    1                           2n-1                         4n-3
Δ=        2                     2n-2  2n                    4n-4   4n-2
Δ=        3               2n-3        2n+1              4n-5       .
Δ=        .           .               .               .            .
Δ=        .       n+2                 .           3n               .
Δ=        n-1 n+1                     3n-3    3n-1                 5n-5
Δ=2n-2    n                           3n-2                         5n-4
*/

"""
import math 
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        #Odd rows go as a squence of i+(numRows+1): 0,4,8,12
        #Even rows go as a squence of i+(numRows-1): 1,3,5,7
        out = ''

        if len(s) <= numRows:
            return s



        for rownum in range(numRows):
            even = rownum % 2 == 0

            if even:
                rowlen = math.floor(len(s)/numRows)
            else:
                rowlen = math.ceil(len(s)/(numRows-1))
            rowstartind = rownum

            if even:
                step = numRows+1
            else:
                step = numRows-1
            sequence = range(rowstartind, int(rowstartind+rowlen*(step)), step)
            for n in sequence:
                if n < len(s):
                    out+=s[n]
        return out
            



solution = Solution()

print(solution.convert("ABC", 2))
assert(solution.convert("PAYPALISHIRING", 3) == 'PAHNAPLSIIGYIR')
assert(solution.convert("", 1) == '')
assert(solution.convert("A", 2) == 'A')
assert(solution.convert("ABC", 2) == 'ACB')
assert(solution.convert("AB", 2) == 'AB')
assert(solution.convert("ABC", 3) == 'ABC')