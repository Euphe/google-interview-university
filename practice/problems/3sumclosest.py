def threeSumClosest(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    
    #Brute solution
    #Calculate all sums and corresponding residuals
    #Pick the best sum
    min_resid = None
    min_sum = None

    for i, num1 in enumerate(nums):
        for j, num2 in enumerate(nums):
            for k, num3 in enumerate(nums):
                if i != j and i != k and j != k:
                    print(num1, num2, num3)
                    tsum = num1+num2+num3
                    resid = abs(target-tsum)
                    print(tsum, resid)
                    if min_resid == None or resid < min_resid:
                        min_resid = resid
                        min_sum = tsum
    print('min resid', min_resid)
    print('min_sum ', min_sum)
    return min_sum
        

print(threeSumClosest([1,1,-1,-1,3], 1), 1)