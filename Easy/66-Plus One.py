"""
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.

 

Example 1:

Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].
"""

"""
Approach
loop from the last digit,
if the sum if more than 10, set current digit to 0 add 1 to the next element
"""

def plusOne(digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    """
    #find the last int in array, add +1 and return
    i=len(digits)-1
    for i in range(i,-1,-1):    
        if digits[i] + 1 != 10:
            digits[i]+= 1
            return digits
        digits[i] = 0

        if i == 0:
            return [1]+digits

    # while digits[i] + 1 > 9:
    #     digits[i] = 0
    #     digits[i-1] = digits[i-1] +1
    # else:
    #     digits[i]= digits[i] + 1  
    # return digits

if __name__ == "__main__":
    digits = [1,8,9]
    print(plusOne(digits))
            