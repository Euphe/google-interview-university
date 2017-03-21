"""
https://leetcode.com/problems/find-all-duplicates-in-an-array/#/description

Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.
Find all the elements that appear twice in this array.
Could you do it without extra space and in O(n) runtime?
"""

class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        rep = []
        for num in nums:
            if nums[abs(num)-1] >= 0:
                nums[abs(num)-1] *= -1 #mark that we have seen it
            else:
                rep.append(abs(num))
        return rep


solution = Solution()
print(solution.findDuplicates([4,7,2,4,1,3,7]))
#assert(solution.findDuplicates([4,3,2,7,8,2,3,1]) == [2,3])