# Chapter 8 - Functions


# Function Basics

def sumfun():
    x = 5
    y = 4
    sum = x + y
    print(sum)


sumfun()  # Function call
sumfun()  # Function call again


# Practice Question 1
# Write a Function named welcome_message()
# that prints a welcome message three times.

def welcome_message():
    print("Welcome to Python Programming...!!")


welcome_message()  # 1st time
welcome_message()  # 2nd time
welcome_message()  # 3rd time


# Practice Question 2
# Define a Function inspire() that prints
# a motivational quote with your name.

def inspire():
    print("You are the master of your destiny:")
    print("Kazim Raza Kanhio")


inspire()


# Practice Question 3
# Create a Function good_morning()
# that prints a greeting and call it twice.

def good_morning():
    print("Good Morning, Kazim Raza Kanhio")


good_morning()  # 1st time
good_morning()  # 2nd time


# Practice Question 4
# Create a Function learn()
# that prints three Python topics.

def learn():
    print("Lists, Dictionaries, Functions")


learn()


# Practice Question 5
# Write a Function show_age()
# that prints the name and age.

def show_age(name="Kazim Raza", age=18):
    print(name, "is", age, "years old")


show_age()


# Practice Question 6
# Write a Function add_num()
# that prints the sum of two numbers.

def add_num(a, b):
    sum = a + b
    print(sum)


add_num(23, 56)


# Practice Question 7
# Write a Function fav_food()
# that prints "Kazim Raza loves <food>".

def fav_food():
    food = "Biryani"
    print("Kazim Raza loves", food)


fav_food()


# Return Statement

def add():
    return 10 + 20


x = add()
print(x)


# Parameters + Return

def add(a, b):
    return a + b


result = add(10, 20)
print(result)


# Another way to call the Function

def add(a, b):
    return a + b


print(add(10, 20))


# Square Function

def square(number):
    return number * number


number = int(input("Enter a number: "))

answer = square(number)
print(answer)