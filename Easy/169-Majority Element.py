def majorityElement(nums):
    """
    :type nums: List[int]
    :rtype: int

    Approach
    use a dict, 
    if element already if dict, increment value
    else add the element 

    """
    book = {}
    for number in nums:
        #if value found in dict, increment the value 
        if number in list(book):
            book[number] += 1
        else:
            book[number] = 0
    #fetch max key from dict
    max_key = max(book, key=book.get)
    return max_key

if __name__ == "__main__":
    nums = [2,2,1,1,1,2,2]
    print(majorityElement(nums))

"""
O(n)
"""