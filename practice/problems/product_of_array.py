"""
https://leetcode.com/problems/product-of-array-except-self/#/description

Given an array of n integers where n > 1, nums, return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Solve it without division and in O(n).

For example, given [1,2,3,4], return [24,12,8,6].

"""
def productExceptSelf(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    
    m1 = [0 for i in range(len(nums))] #m1[i] is the product of everything nums[0:i]
    m1[0] = nums[0]
    for i, num in enumerate(nums):
        if i == 0:
            continue
        m1[i] = m1[i-1] * nums[i]

    m2 = [0 for i in range(len(nums))] #m2[i] is the product of everything nums[-1:i:-1], so going from right to left
    m2[-1] = nums[-1]
    for i in range(len(nums)-2, -1, -1):
        m2[i] = m2[i+1] * nums[i]
    print(m1, m2)
    out = []
    for i, num in enumerate(nums):
        left =1
        if i-1 >= 0:
            left = m1[i-1]
        right = 1
        if i+1 < len(nums):
            right = m2[i+1]
        out.append(left*right)

    return out

print(productExceptSelf([0,0]))
print(productExceptSelf([1,2,3,4]))
