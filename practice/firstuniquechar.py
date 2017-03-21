"""
https://leetcode.com/problems/first-unique-character-in-a-string/#/description

Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.
"""

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_appearances = {}
        uniq_chars = []
        uniq_char_inds = []
        cur_char = None
        cur_char_ind = -1
        for i, char in enumerate(s):
            if char in char_appearances:
                char_appearances[char] += 1
                if char in uniq_chars:
                    uniq_chars.remove(char)
            else:
                char_appearances[char] = 1
                uniq_chars.append(char)
        if len(uniq_chars) > 0:
            cur_char_ind = s.index(uniq_chars[0])
        return cur_char_ind

solution = Solution()

assert(solution.firstUniqChar('abcd') == 0)
assert(solution.firstUniqChar('aabcd') == 2)
assert(solution.firstUniqChar('aabbccdd') == -1)
assert(solution.firstUniqChar('aadadaad') == -1)
assert(solution.firstUniqChar('aca') == 1)