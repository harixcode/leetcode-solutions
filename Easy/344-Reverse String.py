"""
Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.
Example 1:
Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
"""
def reverseString(s):
    """
    :type s: List[str]
    :rtype: None Do not return anything, modify s in-place instead.
    """
    j = len(s)-1
    for i in range (len(s)):
        if j > i :
            temp = s[i]
            s[i] = s[j]
            s[j] = temp
            j -= 1
    return s



if __name__ == "__main__":
    s = ["h","e","l","l","o"]

    ans = reverseString(s)
    print (ans)