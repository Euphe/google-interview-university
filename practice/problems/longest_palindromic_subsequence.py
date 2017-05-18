INP = "CCBA"

def LAS(s, first, last):
    #base case
    if first == last:
        return 1

    #compare first and last
    if s[first] == s[last] and last==first+1:
        return 2

    if s[first] == s[last]:
        return 2 + LAS(s, first+1, last-1) #characters match, they are part of the longest palindromic subsequence
    else:
        return max(LAS(s, first+1, last), LAS(s, first, last-1)) #characters dont match, one of them surely doesnt belong to LAS

print(LAS(INP,0,len(INP)-1))