"""
https://leetcode.com/problems/two-sum

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

"""


"""



"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash_map = {}
        for i, num1 in enumerate(nums):
            complement = target - num1
            if num1 in hash_map:
                if i != hash_map[num1]:
                    return sorted([i, hash_map[num1]])

            hash_map[complement] = i


        raise(Exception('No solution!'))

solution = Solution()
#Test 1
print(solution.twoSum([2, 7, 11, 15], 9))
assert(solution.twoSum([2, 7, 11, 15], 9) == [0, 1])

#Test 2
print(solution.twoSum([1, 2, 3, 4, 5], 4))
assert(solution.twoSum([1, 2, 3, 4, 5], 4) == [0, 2])

#Test 3
print(solution.twoSum([3,3], 6))
assert(solution.twoSum([3,3], 6) == [0, 1])