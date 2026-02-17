# Problem 11: Palindrome Checker: Function to check if string is palindrome.

def IsPallindrome(str):
    if str == str[::-1]:
        return True
    else:
        return False
    
str = input("Enter String:")

if (IsPallindrome(str)):
    print("String is Pallindrome")
else:
    print("String is not Pallindrome")