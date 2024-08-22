#219. Contains Duplicate II
def containsNearbyDuplicate(nums,k):
    #we create a set so that its easier to lookup
    window = set()
    L=0
    for R in range(len(nums)):
        if R - L > k:
            window.remove(nums[L])
            L += 1
        if nums[R] in window:
            return True
        window.add(nums[R])
    return False
if __name__ == "__main__":
    nums = [1,2,1,1]
    k = 1
    print(containsNearbyDuplicate(nums,k))        