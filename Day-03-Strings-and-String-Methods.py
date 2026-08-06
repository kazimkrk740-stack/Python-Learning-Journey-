# Chapter 3 - Strings

# String Types
str1 = 'Hello'
str2 = "Kazim Raza"
str3 = '''This is a string'''

print(str1)
print(str2)
print(str3)

# String Concatenation
print("Hello" + " " + "Kazim Raza")

# Length of String
print(len("KazimRaza"))

# Indexing
str4 = "Kazim"

print(str4[0])
print(str4[3])

# Slicing
str5 = "Kanhio"

print(str5[0:3])
print(str5[:4])
print(str5[3:])

# Negative Indexing
str6 = "GulabJamun"

print(str6[-5:-1])
print(str6[-8:-2])
print(str6[-9:-5])

# String Methods
str7 = "Kazim raza"

print(str7.lower())
print(str7.upper())
print(str7.title())
print(str7.find("i"))
print(str7.replace("raza", "Kanhio"))