
def findAnagram(s,p):
    pCount, sCount = {},{}
#check if length of p is greater than s, if yes return empty list
    if len(p) > len(s):return []
#add each element from p and s to a dictionary and assign value as 1
    for i in range (len(p)):
        pCount[p[i]] = 1 #+ pCount.get(p[i],0)
        sCount[s[i]] = 1 #+ sCount.get(s[i],0)

#if both dict are same, add index 0 to the result
    if pCount == sCount: 
        res=[0]
    else:
        res=[]
# left pointer = 0
    l=0
    
#right pointer to start from last character as per len(p) in S
#set value for leftmost element to 0
    for r in range(len(p), len(s)):
        sCount[s[r]] = 1 + sCount.get(s[r],0)
        sCount[s[l]] -= 1
#if value is 0, remove the element from sCount
        if sCount[s[l]]==0:
            sCount.pop(s[l])
#increment left pointer
        l += 1
#if both dict are same, append the index of first element to result
        if pCount == sCount:
            res.append(l)
    return res
    
if __name__ == "__main__":
    s = "cbaebababcda"
    p = "bc"
    print(findAnagram(s,p))
        