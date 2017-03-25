"""

Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? 
Find all unique triplets in the array which gives the sum of zero.

Note: The solution set must not contain duplicate triplets.
"""


class Solution(object):
    def twoSum(self, nums, target, skip_twovals = [], skip_ind=None):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash_map = {}
        for i, num1 in enumerate(nums):
            if i != skip_ind:
                complement = target - num1
                if num1 in hash_map:
                    if i != hash_map[num1]:
                        twoval = sorted([num1, hash_map[num1]])
                        if not twoval in skip_twovals:
                            return twoval
                hash_map[complement] = num1

        return []

    def all_twoSum(self, nums, target,  skip_ind=None):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        twovals = []
        hash_map = {}
        for i, num1 in enumerate(nums):
            if i != skip_ind:
                complement = target - num1
                if num1 in hash_map:
                    if i != hash_map[num1]:
                        twoval = sorted([num1, hash_map[num1]])
                        if not twoval in twovals:
                            twovals.append(twoval)
                hash_map[complement] = num1

        return twovals


    def threeSum(self, nums):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        target = 0
        twovals = []
        triplets = []

        compliments_twovals = {}
        for i, num in enumerate(nums):
            complement = target-num

            if abs(complement) in compliments_twovals:
                continue
            two_sum_vals = self.all_twoSum(nums, complement, i)#, twovals)
            # for t in two_sum_vals:
            #     twovals.append(t)
            if two_sum_vals:
                compliments_twovals[complement] = two_sum_vals
                for twoval in two_sum_vals:
                    triplet = sorted([twoval[0], twoval[1], num])
                    if not triplet in triplets:
                        triplets.append(triplet)
        return triplets



solution = Solution()

"""
def threeSum(nums):
    res = []
    nums.sort()
    for i in range(len(nums)-2):
        if i > 0 and nums[i] == nums[i-1]:

            continue
        l, r = i+1, len(nums)-1
        while l < r:
            s = nums[i] + nums[l] + nums[r]
            if s < 0:
                l +=1 
            elif s > 0:
                r -= 1
            else:
                res.append((nums[i], nums[l], nums[r]))

                while l < r and nums[l] == nums[l+1]:
        
                    l += 1
                while l < r and nums[r] == nums[r-1]:

                    r -= 1
                l += 1; r -= 1
    return res
"""
#print(solution.all_twoSum([-4, -2, -2, 2, 2, 0, 4], 4))

print(threeSum([-4, -2, -2, 2, 2, 0, 4]))
#print(solution.threeSum([-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]))
#assert(solution.threeSum([-1, 0, 1, 2, -1, -4]) == [[-1, 0, 1],[-1, -1, 2]])