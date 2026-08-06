# Take input in a number if > 0 it's positive, 0 = zero and < 0 then print negative.

num = int(input("Enter a number : "))

if (num > 0):
    print("Positive")

elif (num == 0):
    print("Zero")

else:
    print("Negative")