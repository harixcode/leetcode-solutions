"""58. Length of Last Word
Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.

Example 1:

Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.
Example 2:

Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.
Approach
use .trim() to remove white space from end of string and beginning.
initialise a count variable

Loop from end of string until a space is found, return count
"""

def lengthOfLastWord(s):
    """
    :type s: str
    :rtype: int
    """
    s= s.strip()
    count = 0
    for char in reversed(s):
        if char == " ":
            return count
        
        count += 1
    return count
    
if __name__ == "__main__":
    s = "a"
    print(lengthOfLastWord(s))

    
"""
O(n)
"""