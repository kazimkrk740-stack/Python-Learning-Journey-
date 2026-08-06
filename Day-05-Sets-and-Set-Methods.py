# Sets

languages = {"Python", "Java", "C++", "Python", "Java", "C"}

print(languages)
print(type(languages))

# add()
languages.add("SQL")
print(languages)

# remove()
languages.remove("SQL")
print(languages)

# pop()
languages.pop()
print(languages)

# clear()
languages.clear()
print(languages)

# Practice Question

languagesList = ["Python", "Java", "C++", "Python", "Java", "C"]

print(languagesList)
print(type(languagesList))

languagesSet = set(languagesList)

print(type(languagesSet))
print("Unique Languages:", len(languagesSet))
print(languagesSet)