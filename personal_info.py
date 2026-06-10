#Ginnikunta Suchitra
# Personal Information Manager
# My first Python project

# Welcome message
print("=" * 40)
print("    PERSONAL INFORMATION MANAGER")
print("=" * 40)
print()

#storing static information using variables
name="Ginnikunta Suchitra" #string data type to store name
age=21 #integer data type to store age
city="Hyderabad" #string data type to store city
hobby="Cooking"#string data type to store hobby

# Getting user input
print("Please tell me about yourself:")
print("-" * 30)
food=input("Enter your favorite food: ")
#basic validation to ensure that the input is not empty
while food=="":
    print("Input cannot be empty.")
    food=input("Enter your favorite food: ")
color=input("Enter your favorite color: ")
#basic validation to ensure that the input is not empty
while color=="":
    print("Input cannot be empty.")
    color=input("Enter your favorite color: ")
    
print()



#age in months
age_in_months = age * 12

#display information
print("=" * 30)
print("YOUR INFORMATION")
print("=" * 30)

print(f"Name   : {name}")
print(f"Age    : {age} ({age_in_months} months old)")

print("-" * 30)

print(f"City : {city}")
print(f"Hobby : {hobby}")

print("=" * 30)

print(f"Favorite Food: {food}")
print(f"Favorite Color: {color}")
print()

# Goodbye message
print("=" * 40)
print("End of program")
print("=" * 40)
