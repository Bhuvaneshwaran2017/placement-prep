#=====================================
# Mini Challenge - 1 [Strings]
#=====================================

"""
Movie Ticket Eligibility
Take:
- Name
- Age
Rules:
- Age < 5 → Free Ticket
- Age 5–17 → Child Ticket
- Age 18–59 → Adult Ticket
- Age ≥ 60 → Senior Citizen Discount
Print a neatly formatted ticket using f-strings.
"""

name = input("Enter your name: ")
age = int(input("Enter your age: "))

if age < 5:
    print(f"Hello {name}, you are eligible for a free ticket.")
elif age >=5 and age <= 17:
    print(f"Hello {name}, you are eligible for a child ticket.")
elif age >= 18 and age <= 59:
    print(f"Hello {name}, you are eligible for an adult ticket.")
elif age >= 60:
    print(f"Hello {name}, you are eligible for a senior citizen discount.")