#====================================
# Mini Challenge - 1 [Strings]
#====================================

"""Without looking back,
write this yourself.
Program should ask

Name
Age
College
Dream Job

Then print

Hello Bhuvi!
You are 20 years old.
You study at SRM University.
Your dream is to become an ML Engineer.
Good luck!

#====================================   
#solution
#====================================

name = input("What is your name? ")
age = input("How old are you? ")
college = input("What college do you go to? ")
dream_job = input("What is your dream job? ")

print("Hello, " + name + "!")
print("You are " + age + " years old.")
print("You study at " + college + ".")
print("Your dream is to become an " + dream_job + ".")
print("Good Luck")
"""

#====================================
#challenge - 2 [Maths]
#====================================

"""
Ask the user for two numbers.
Print:
- Sum
- Difference
- Product
- Division
Hint: Use int(input(...)).


#====================================
#solution
#====================================

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Sum: " + str(a + b))
print("Difference: " + str(a - b))
print("Product: " + str(a * b))
print("Division: " + str(a / b))
"""

#====================================
#challenge - 3 [Age next year]
#====================================

"""Ask the user:
- Name
- Age
Then print:
Hello Bhuvi!

Next year you will be 21 years old.


#====================================
#solution
#====================================

name = input("What is your name? ")
age = int(input("How old are you? "))

print("Hello, " + name + "!")
print("Next year you will be " + str(age + 1) + " years old.")
"""

#====================================
#challenge - 4 [Even or Odd]
#====================================

"""Ask for a number.
Print whether it is Even or Odd.


#====================================
#solution 
#====================================

number = int(input("Enter a number: "))
if number % 2 == 0:
    print("the Number is Even")
else:
    print("the Number is Odd")
"""

#====================================
#challenge - 5 [string]
#====================================
"""
First_name = "Bhuvi"
Last_name = "R"
College = "SRM University"
dream_company = "Google"

print("Hello" + " " + "I'm" + " " + First_name + " " + Last_name)
print("I study at" + " " + College)
print("I want to work at" + " " + dream_company)
"""

#====================================
#challenge - 6 [Palindrome]
#====================================
"""
word = input("Enter a word: ")
print("The reverse of the word is: " + word[::-1])
if word == word[::-1]:
    print("The word is a palindrome.")
else:
    print("The word is not a palindrome.")
"""

#====================================
#challenge - 7
#====================================
"""
Ask the user:
- Name
- Age
- College
- Dream Company
Print a professional introduction using one f-string.
Example:
Hello, I'm Bhuvi.
I'm 20 years old.
I study at SRM University.
My dream company is Google.


#====================================
#Solution
#====================================

name = input("What is your name? ")
age = input("How old are you? ")
college = input("What college do you go to? ")
dream_company = input("What is your dream company? ")

print(f"Hello, I'm {name}. \nI'm {age} years old. \nI study at {college}. \nMy dream company is {dream_company}.")
"""

#====================================
#challenge - 8
#====================================
"""
Ask for:
- Product Name
- Price
- Quantity
Print:
Product : Laptop

Price   : ₹45000.00

Quantity: 2

Total   : ₹90000.00
Use:
- f-strings
- formatting (:.2f)


#====================================
#solution
#====================================

product_Name = input("Enter the product name: ")
price = float(input("Enter the price: "))
quantity = int(input("Enter the quantity: "))
total = price * quantity
print(f"Product : {product_Name}")
print(f"Price   : ₹{price:.2f}")
print(f"Quantity: {quantity}")
print(f"Total   : ₹{total:.2f}")
"""

#====================================
#challenge - 9
#====================================
Name = input("Enter your name: ")
Age = int(input("Enter your age: "))
College = input("Enter your college name: ")
CGPA = float(input("Enter your CGPA: "))

print(f"Name\t: {Name}")
print(f"Age\t: {Age}")
print(f"College\t: {College}")
print(f"CGPA\t: {CGPA}")