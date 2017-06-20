"""
Given an integer array with even length, where different numbers in this array represent different kinds of candies. Each number means one candy of the corresponding kind. You need to distribute these candies equally in number to brother and sister. Return the maximum number of kinds of candies the sister could gain.

Example 1:
Input: candies = [1,1,2,2,3,3]
Output: 3
Explanation:
There are three different kinds of candies (1, 2 and 3), and two candies for each kind.
Optimal distribution: The sister has candies [1,2,3] and the brother has candies [1,2,3], too. 
The sister has three different kinds of candies. 
Example 2:
Input: candies = [1,1,2,3]
Output: 2
Explanation: For example, the sister has candies [2,3] and the brother has candies [1,1]. 
The sister has two different kinds of candies, the brother has only one kind of candies. 
Note:

The length of the given array is in range [2, 10,000], and will be even.
The number in given array is in range [-100,000, 100,000].
"""
#Recursive solution
def max_candy_types(candies, picked_types, picked_candies, max_candies):
    if not candies or picked_candies >= max_candies:
        return 0
        
    candy = candies[0]
    
    #either the sister gets candy, or the brother gets it.
    #So the max different candy types is either if the sister gets the candy, or if she doesnt
    
    if candy in picked_types: #if she already picked that type and she gets it
        sister_gets_candy = max_candy_types(candies[1:], picked_types, picked_candies+1, max_candies)
    else: #if sister hasnt picked that type yet and she picks it
        sister_gets_candy = 1 + max_candy_types(candies[1:], picked_types + [candy], picked_candies+1, max_candies)
    
    sister_no_candy = max_candy_types(candies[1:], picked_types, picked_candies, max_candies)
    
    return max(sister_no_candy, sister_gets_candy)

def max_candy_types_dp(candies):
    #We need to try all possible combinations of candies
    #The combination size is known upfront: len(candies)//2

    #The problem with the recursive solution is that we are calculating the dead-end branches too, like where we are picking duplicate type candies

    #
class Solution:
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        
        return max_candy_types(candies, [], 0, len(candies)//2)
        
solution = Solution()

candies = [1,1,2,3]

answer = solution.distributeCandies(candies)
print('Answer', answer)
assert(answer == 2)