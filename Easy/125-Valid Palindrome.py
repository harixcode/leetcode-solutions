"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Approach
convert existing string into alphanumeric string
reverse it and check if its the same 
str.lower()
"""

def isPalindrome(s):
    #return bool
    s = s.lower()
    ans = []
    for char in s:
        #check if char is alphanumeric
        if char.isalnum():
            ans.append(char)
    #left and right pointers should be same value if Palindromic
    l,r = 0, len(ans)-1
    while l < len(ans):
        if ans[l] != ans[r]:
            return False
        r -=1
        l +=1
    return True

if __name__ == "__main__":
    s = "race a car"
    print(isPalindrome(s))