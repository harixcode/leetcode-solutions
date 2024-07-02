#Longest common prefix
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        character = strs[0]
        for string in strs[1:]:
            #print("string = ", string)
            while string.find(character) != 0:# when char not found, remove that char
                character = character[:-1]
        print("Longest common prefix: ", character)
        return character 

