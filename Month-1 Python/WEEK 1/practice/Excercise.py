#1
age = int(input("Enter your age: "))

if age >= 18:
    print("You are Eligible to vote")
else:
    print("You are not eligible to vote")

#2
num = int(input("Enter a number: "))

if num > 0:
    print("The number is positive")
elif num < 0:
    print("The number is negative")
else:
    print("The number is zero")

#3
marks = int(input("Enter your marks: "))

if marks >= 90:
    print("Distinction")
elif marks >= 80:
    print("First Class")
elif marks >= 70:
    print("Pass")   
else: 
    print("Fail")

#4
salary = int(input("Enter your salary: "))

if salary >= 50000:
    print("High income")
else:   
    print("Normal income")

#5
username = input("Enter your username: ")

if username == "admin":
    print("Access granted")
else:
    print("Access denied")

