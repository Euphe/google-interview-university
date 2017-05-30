"""

Given a value N, if we want to make change for N cents, and we have infinite supply of each of S = { S1, S2, .. , Sm } valued coins, how many ways can we make the change? The order of coins doesn’t matter.

For example, for N = 4 and S = {1,2,3}, there are four solutions: {1,1,1,1},{1,1,2},{2,2},{1,3}. So output should be 4. For N = 10 and S = {2, 5, 3, 6}, there are five solutions: {2,2,2,2,2}, {2,2,3,3}, {2,2,6}, {2,3,5} and {5,5}. So the output should be 5.

"""

N = 2
S = (1, 2)
#Expected output: 3

def total_solutions(n, coins):
    #base cases
    if n == 0:
        return 1

    if n < 0:
        return 0

    if len(coins) == 0:
        return 0

    #solutions with coins[-1] + solutions without coins[-1]
    return total_solutions(n-coins[-1], coins) + total_solutions(n, coins[:-1])

def coin_change_dp(n, coins):
    coins = sorted(coins)
    dp = [ [ 0 for i in range(n+1) ] for i in range(len(coins)+1) ]  #dp[i][j] = solutions for coins[:i] and  N = j

    #base case: if we dont have any coins there are no solutions
    #first row is all zeroes

    #base case 2: if n == 0 there is one solution
    for i in range(len(coins)+1):
        dp[i][0] = 1

    # print('dp')
    # for row in dp:
    #     print(row)
    # print('')
    #fill the matrix
    for i in range(1, len(coins)+1):
        for j in range(1, n+1):

            left_ind = j-coins[i-1]
            if left_ind < 0:
                left_part = 0
            else:
                left_part =  dp[i][j-coins[i-1]]


            dp[i][j] = left_part + dp[i-1][j]
            # for row in dp:
            #     print(row)
            # print('')
    # for row in dp:
    #     print(row)
    # print('')
    return dp[len(coins)][n]



assert(coin_change_dp(4, [1,2,3]) == 4)
assert(coin_change_dp(10, [2, 5, 3, 6]) == 5)
S = [44,5,9,39,6,25,3,28,16,19,4,49,40,22,2,12,45,33,23,42,34,15,46,26,13,31,8]
N = 2
assert(coin_change_dp(N, S) == 1)
#print(total_solutions(6, S))

