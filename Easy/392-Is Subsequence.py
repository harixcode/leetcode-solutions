
def isSubsequence(self, s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    """
    Approach
    two pointers - l at 1 st char of s - r at 1st char of t
    if a similar character is found,
    increment l
    else return False.

    if 
    """
    l = 0
    r = 0
    #edge cases
    if not s:
        return True
    elif not t:
        return False
    
    while r < len(t):
        if s[l] == t[r]:
            l += 1   
        r += 1
        #if l pointer goes beyond the end of s, return true
        if l == len(s):
            return True
    return False