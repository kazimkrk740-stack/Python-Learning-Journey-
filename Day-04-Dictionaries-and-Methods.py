# Dictionary

student = {
    "name": "Kazim",
    "age": 18,
    "city": "Nawabshah"
}

print(student)
print(type(student))

# Access value
print(student["name"])

# Update value
student["age"] = 19
print(student)

# Add new key
student["subject"] = "Maths"
print(student)

# Remove key
student.pop("subject")
print(student)

# Dictionary Methods
print(student.keys())
print(student.values())
print(student.items())
print(student.get("name"))

# Update Dictionary
student.update({
    "city": "Mirpur"
})

print(student)

# Practice Question

marks = {}

marks["Math"] = int(input("Enter Math marks: "))
marks["Science"] = int(input("Enter Science marks: "))
marks["English"] = int(input("Enter English marks: "))

print("Final Dictionary:", marks)