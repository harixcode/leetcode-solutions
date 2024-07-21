
def removeElement(nums, val):
    l = 0
    for r in range (len(nums)):
        if nums[r] != val:
            nums[l] = nums[r]
            l += 1
    return l
    
if __name__ == "__main__":
    nums = [0,1,2,2,3,0,4,2]
    ans = removeElement(nums,2)
    print (ans, nums)