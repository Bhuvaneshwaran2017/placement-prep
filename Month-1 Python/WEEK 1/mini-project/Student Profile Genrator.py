"""
Build a Student Profile Generator.
Requirements:
1. Take input:
   - Name
   - Age
   - College
   - Department
   - CGPA
   - Dream Job
2. Display a neatly formatted report using f-strings.
Example:
========================================
         STUDENT PROFILE
========================================

Name       : Bhuvi
Age        : 20
College    : SRM University
Department : AIML
CGPA       : 8.72
Dream Job  : AI Engineer

========================================
"""

#get input
name = input("Enter your name: ")
age = input("Enter your age: ")
college = input("Enter your college: ")
department = input("Enter your department: ")
cgpa = input("Enter your CGPA: ")
dream_job = input("Enter your dream job: ")

print("""
========================================
         STUDENT PROFILE
========================================
""")

print(f"{'Name':<11}: {name}")
print(f"{'Age':<11}: {age}")
print(f"{'College':<11}: {college}")
print(f"{'Department':<11}: {department}")
print(f"{'CGPA':<11}: {cgpa}")
print(f"{'Dream Job':<11}: {dream_job}")

print("\n========================================")
