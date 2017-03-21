"""
https://leetcode.com/problems/nim-game/#/description

You are playing the following Nim Game with your friend: There is a heap of stones on the table, each time one of you take turns to remove 1 to 3 stones.
The one who removes the last stone will be the winner. You will take the first turn to remove the stones.
Both of you are very clever and have optimal strategies for the game. 
Write a function to determine whether you can win the game given the number of stones in the heap.

"""

def canWinNim(n):
    """
    :type n: int
    :rtype: bool
    """
    #second player wins if: n mod k+1 == 0 mod k+1 
    return n % 4 != 0 

assert(solution.canWinNim(1) == True)