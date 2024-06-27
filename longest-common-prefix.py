#Longest common prefix
strs = ["flower","flow","flight"]

character = strs[0]
#for every item from list, traverse through chars and remove chars not present
for string in strs[1:]:
    #print("string = ", string)
    while string.find(character) != 0:# when char not found, remove that char
        character = character[:-1]

print("Longest common prefix: ", character)