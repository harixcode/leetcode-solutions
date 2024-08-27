
def merge(nums1, m, nums2, n):
        
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.

Approach
2 pointers l & r, l points to last element of nums1, r points first element of nums2 
while nums1, nums2:
if nums[l] > nums [r], decrement l pointer +1, shift last element to right

else, assign nums[r] to index l and increment r +1

        """
        l = m-1
        r = n-1
        k = (m+n) -1
        while r >=0:
            if l>=0 and nums1[l] > nums2[r]: 
                nums1[k] = nums1[l]
                l -=1
            else:
                nums1[k] = nums2[r]
                r -=1
            
            k -=1
            #print(nums1)

        while r>0:
              nums1[k] = nums2[r]
              r -= 1
              k -= 1  
        return nums1


if __name__ == "__main__":
    nums1 = [0] #[1,2,2,3,4,0,0] l=2 r =1
    m = 0
    nums2 = [1]
    n = 1
    print(merge(nums1, m, nums2, n))