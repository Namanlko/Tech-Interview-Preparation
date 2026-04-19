# Problem 2: Count Vowels and Consonants in a string.

str = input("Enter String :)")
vC = 0
cC = 0

for i in range(len(str)):
    if str[i] == 'a' or str[i] == 'e' or str[i] == 'i' or str[i] == 'o' or str[i] == 'u' or str[i] == 'A' or str[i] == 'E' or str[i] == 'I' or str[i] == 'O' or str[i] == 'U':
        vC += 1
    else:
        cC += 1

print("Vowel Count = ",vC)
print("Consonent Count = ",cC)