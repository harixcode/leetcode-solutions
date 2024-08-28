

def canConstruct(ransomNote, magazine):
    """
    :type ransomNote: str
    :type magazine: str
    :rtype: bool

    Approach
    count occurances of each alphabet from magazine and push to dict

    take first char from ransomNote, check if its already in dict, if yes, decrement key by 1.
    when there is no matching char in dict, return false

    """
    count = 0
    charMap = {}
    for char in magazine:
        #store alphabets to charMap and record occurances
        if char in list(charMap):
            charMap[char] += 1
        else:
            charMap[char] = 1
    print(charMap)    
    for char in ransomNote:
        if char in list(charMap):
            charMap[char] -=1
        else:
            return False
        if charMap[char] < 0:
            return False

    return True


if __name__ == "__main__":
    ransomNote = "aa"
    magazine = "aab"
    print(canConstruct(ransomNote, magazine))


    """
    O(m+n)
    """