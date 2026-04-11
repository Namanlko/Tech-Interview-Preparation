# Problem 15: Check if a word is present in a sentence.

def IsPresent(sen,word):
    s = sen.split(" ")
    for i in s:
        if (i==word):
            return True
    return False

print(IsPresent("My name is Naman","Naman"))