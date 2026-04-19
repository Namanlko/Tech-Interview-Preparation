# Problem 5: Check if Two Strings are Anagrams.

def ifAnagrams(str1, str2):
    str1 = str1.replace(" ","").lower()
    str2 = str2.replace(" ","").lower()
    if (len(str1)!=len(str2)):
        return False
    return sorted(str1) == sorted(str2)

print(ifAnagrams("Listen","silent"))
print(ifAnagrams("Hello","World"))
print(ifAnagrams("Dormitory", "Dirty room")) 