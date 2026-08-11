# Practice Question 
# Vowels and Consonants

# Write a Function that takes a string
# and returns the count of vowels and consonants separately.

def count_vow_cons(inputuser):

    vowels = "aeiouAEIOU"

    countvowel = 0
    countconsonants = 0

    for eachChar in inputuser:

        if eachChar.isalpha():

            if eachChar in vowels:
                countvowel = countvowel + 1
            else:
                countconsonants = countconsonants + 1

    return countvowel, countconsonants


# Function Call

vowels, consonants = count_vow_cons(
    input("Write a string: ")
)

print("Vowels:", vowels)
print("Consonants:", consonants)