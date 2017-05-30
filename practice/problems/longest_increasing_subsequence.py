"""
Given a sequence, find the length of the longest increasing subsequence from a given sequence .
The longest increasing subsequence means to find a subsequence of a given sequence in which the subsequence's elements are in sorted order, lowest
to highest, and in which the subsequence is as long as possible. This subsequence is not necessarily contiguous, or unique.

Note: Duplicate numbers are not counted as increasing subsequence.

For example:
 length of LIS for 
{ 10, 22, 9, 33, 21, 50, 41, 60, 80 } is 6 and LIS is {10, 22, 33, 50, 60, 80}.


Input:

The first line contains an integer T, depicting total number of test cases. 
Then following T lines contains an integer N depicting the size of array and next line followed by the value of array.


Output:

Print the Max length of the subsequence in a separate line.


Constraints:

1 ≤ T ≤ 40
1 ≤ N ≤ 1000
0 ≤ A[i] ≤ 300


"""

INP = [50, 3, 10, 7, 40, 80]

def get_lis(alist):

    #idea:
    #for each element in alist
        #calculate the LIS length for that element 
    #LIS for element i is LIS(i) = LIS(x)+1, where x is the index, x < i and alist[x] < alist[i]

    #lets do top down DP

    lis_memo = {}
    for i, item in enumerate(alist):
        if i == 0:
            lis_memo[item] = 1
            continue

        #get prev LIS
        prev_smaller = None
        prev_max = None
        prev_max_lis = None
        for j in range(i, -1, -1):
            if alist[j] < item:
                if not prev_max_lis or lis_memo[alist[j]] > prev_max_lis:
                    prev_max_lis = lis_memo[alist[j]]
                    prev_max = alist[j]

        if prev_max:
            lis_memo[item] = prev_max_lis + 1
        else:
            lis_memo[item] = 1
    print(lis_memo)
    return max(lis_memo.values())
print(get_lis(INP))

#Bottom up LIS taken from http://www.geeksforgeeks.org/dynamic-programming-set-3-longest-increasing-subsequence/
def lis(arr):
    n = len(arr)
 
    # Declare the list (array) for LIS and initialize LIS
    # values for all indexes
    lis = [1]*n
 
    # Compute optimized LIS values in bottom up manner
    for i in range (1 , n):
        for j in range(0 , i):
            print('arr[i], arr[j]', arr[i], arr[j])
            print('lis[i], lis[j]+1', lis[i], lis[j]+1)
            if arr[i] > arr[j] and lis[i]< lis[j] + 1:
                lis[i] = lis[j]+1
                print('lis[i] is now', lis[i])
 
    # Initialize maximum to 0 to get the maximum of all
    # LIS
    maximum = 0
 
    # Pick maximum of all LIS values
    for i in range(n):
        maximum = max(maximum , lis[i])
 
    return maximum

print(lis(INP))