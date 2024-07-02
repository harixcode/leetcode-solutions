"""
Valid Parentheses:
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
"""
def isValid():
    stack = []
    for char in s:
        if char in "({[": # if char is opening bracket
            stack.append(char)
        else: #if char is closing bracket
            if not stack or \
                (char == ")" and stack[-1] != '(') or\
                (char == "}" and stack[-1] != '{') or \
                (char == "]" and stack[-1] != "["):
                return False
            stack.pop()
    return not stack

if __name__ == "__main__":
    ans = isValid()
    print (ans)
     

"""
SOLVED 
TIME COMPLEXITY: O(N)
"""