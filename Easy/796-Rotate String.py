"""
Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.

A shift on s consists of moving the leftmost character of s to the rightmost position.

For example, if s = "abcde", then it will be "bcdea" after one shift.
"""

def rotateString(s, goal):
    """
    """
    
    char = list(s)
    j = len(char)-1
    goal = list(goal)
    print (len(char))
    for i in range (len(char)):
        if i < j:
            temp = char[i]
            char[i] = char[i+1]
        else:
            char[i] = temp
        #print (char)
        if char == goal:
            break
    return char



if __name__ == "__main__":
    s = "abcde"
    goal = "cdeab"
    ans = rotateString(s, goal)
    print (ans)