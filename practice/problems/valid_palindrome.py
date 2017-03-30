"""
https://leetcode.com/problems/valid-palindrome/#/description

Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

For example,
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.

Note:
"""

import string

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) < 2:
            return True

        s = s.lower()

        alphanumeric=string.ascii_lowercase + string.digits
        i = 0
        j = len(s)-1

        while i < j:
            #move left mark until we reach a valid char
            #move right mark until we reach a valid char
            if not s[i] in alphanumeric:
                i+=1
                continue

            if not s[j] in alphanumeric:
                j-=1
                continue

            #if valid chars are not equal:
            if s[i] != s[j]:
                return False
            else:
                i+=1
                j-=1

        return True

solution = Solution()

print(solution.isPalindrome('')) #True
print(solution.isPalindrome('a')) #True
print(solution.isPalindrome('bab')) #True
print(solution.isPalindrome('b a.b')) #True
print(solution.isPalindrome('b a..b')) #True
print(solution.isPalindrome('b a..c')) #False
print(solution.isPalindrome('ba')) #False
print(solution.isPalindrome('bb')) #True