#Remove Duplicates from Sorted Array

def removeDuplicates (nums):
    k = 1 # set left pointer to index 1.
    for i in range(1,len(nums)): #iterate from second element and compare it with previous value
        if nums[i] != nums[i-1]:#if unique,
            nums[k] = nums[i] #store the value at left pointer in nums list
            k += 1
                         
    return k

if __name__ == "__main__":
    nums = [1,1,2,2,3]
    ans = removeDuplicates(nums)
    print (ans, nums)