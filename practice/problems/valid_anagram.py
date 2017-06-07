"""
https://leetcode.com/problems/valid-anagram/#/description

Given two strings s and t, write a function to determine if t is an anagram of s.

For example,
s = "anagram", t = "nagaram", return true.
s = "rat", t = "car", return false.

Note:
You may assume the string contains only lowercase alphabets.

"""


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        characters = {}
        
        for c in s:
            if not c in characters:
                characters[c] = 0
            characters[c] += 1
        
        for c in t:
            if not c in characters:
                return False
            characters[c] -= 1
        
        for c, count in characters.items():
            if count != 0:
                return False
        return True