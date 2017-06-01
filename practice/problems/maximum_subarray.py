"""

https://leetcode.com/problems/maximum-subarray/#/description


Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
the contiguous subarray [4,-1,2,1] has the largest sum = 6.

"""

def best_sum(alist):
	if not alist:
		return 0, []

	best_sum_right, max_subarr_right = best_sum(alist[1:])
	sum_with = (alist[0] + best_sum_right, [alist[0]]+max_subarr_right)
	sum_without = (best_sum_right, max_subarr_right)

	return max(sum_with, sum_without)

def max_subar(nums):
	max_sum = None
	max_subar = []
	for l in range(1, len(nums)+1):
		for i in range(len(nums)-l+1):
			subar = nums[i:i+l]

			subar_sum = sum(subar)
			if max_sum is None or subar_sum > max_sum:
				max_sum = subar_sum
				max_subar = subar
	return max_sum or 0, max_subar
