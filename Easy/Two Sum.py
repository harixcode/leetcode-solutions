def twoSum( nums, target):
    n = len(nums)
    #using hash map
    nmap = {}
    for index in range(n):
        compliment = target - nums[index]

        if compliment in nmap:
            return nmap[compliment], index
        nmap[nums[index]] = index
        
    return []
    #


if __name__ == "__main__":
    nums = [2,7,8,5,4]
    target = 9
    ans = twoSum(nums, target)
    print (ans)


""" O(n^2) 
    for i in range(n):
        for j in range(i+1,n):
            if nums[i] + nums[j] == target:
                return i,j
"""

""" O(n)

def twoSum( nums, target):
    n = len(nums)
    #using hash map
    l = 0
    for r in range(1, n):
        if nums[l]+nums[r] == target:
            return l,r
        l += 1
    return []

"""