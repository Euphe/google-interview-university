
    

def knapsack_dp(values, weights, max_capacity):
    dp = [[0 for x in range(max_capacity+1)] for x in range(len(values)+1)]
    
    for i in range(len(values)+1):
        for j in range(max_capacity+1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif weights[i-1] <= max_capacity:
                dp[i][j] = max(values[i-1]+dp[i-1][j-weights[i-1]], dp[i-1][j])
            else:
                dp[i][j] = dp[i-1][j]
    return dp[len(values)][max_capacity]
    
def knapsack(values, weights, max_capacity):
    #base case
    if len(values) == 0 or max_capacity == 0:
        return 0
        
    n = len(values)-1
    
    if weights[n] > max_capacity:
        return knapsack(values[:n], weights[:n], max_capacity) #this item can't be part of the optimal solution
    
    #otherwise the optimal solution is either the one where the nth item is included or the other where its not included
    return max( values[n] + knapsack(values[:n], weights[:n], max_capacity - weights[n]),
            knapsack(values[:n], weights[:n], max_capacity))
        
    



# test_cases = int(lines[0])
# for i in range(test_cases):
#     n_items = int(lines[4*i + 1])
#     w_capacity = int(lines[4*i + 2])
#     values = [int(x) for x in lines[4*i + 3].split(' ')]
#     weights = [int(x) for x in lines[4*i + 4].split(' ')]
#     print(knapsack_dp(values, weights, w_capacity))
    

        