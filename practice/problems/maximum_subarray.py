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

def max_subar_dp(nums):
	if not nums:
		return 0

	if len(nums) == 1:
		return nums[0]

	dp = [0 for num in nums]
	dp[0] = nums[0]


	max_val = nums[0]
	for i, num in enumerate(nums):
		if i == 0:
			continue

		dp[i] = nums[i] + (dp[i-1] if dp[i-1] > 0 else 0)
		if dp[i] > max_val:
			max_val = dp[i]

	return max_val


import random
ints = [random.randint(-100, 100) for i in range(10000)]
print(max_subar_dp(ints))
