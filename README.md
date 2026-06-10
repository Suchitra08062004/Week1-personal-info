
# Personal Information Manager

## Project Description

This is my first Python project! It's a program that stores and displays personal information.

The program uses variables to store personal details, accepts user input for additional information, performs a simple calculation, and displays everything in a clean and formatted way.

---

## Project Overview

### Goal

The goal of this project is to learn the fundamentals of Python programming by creating a simple Personal Information Manager.

### Objectives

* Learn how to use variables to store data.
* Practice getting input from users.
* Display information using formatted output.
* Implement basic input validation.
* Perform simple calculations using Python.

---

## What I Learned

### Variables

How to store different types of data.

### Input/Output

Getting user input and displaying results.

### String Formatting

Using f-strings to create clean and readable output.

### Error Handling

Basic validation for user input.

---

## Setup Instructions

### Prerequisites

* Python 3.x installed on your computer.
* Terminal, Command Prompt, or VS Code.

### Installation and Execution

1. Download or clone the repository.
2. Open a terminal or command prompt.
3. Navigate to the project folder.
4. Run the following command:

```bash
python personal_info.py
```

5. Follow the prompts to enter your information.

---

## Code Structure

```text
week1-personal-info/
│── personal_info.py
│── README.md
│── test_inputs.txt
│── .gitignore
└── screenshots/
    ├── user-input.png
    ├── input-validation.png
    └── final-output.png
```

### File Description

| File             | Purpose                                              |
| ---------------- | ---------------------------------------------------- |
| personal_info.py | Main Python program                                  |
| README.md        | Project documentation                                |
| test_inputs.txt  | Test cases and expected results                      |
| .gitignore       | Prevents unnecessary files from being tracked by Git |
| screenshots/     | Contains project screenshots                         |

---

## Features

* Stores static information (name, age, city, hobby)
* Gets dynamic information from user
* Displays all information in a formatted way
* Basic input validation
* Age calculation in months

---

## Technical Details

### Variables Used

| Variable       | Data Type | Purpose                      |
| -------------- | --------- | ---------------------------- |
| name           | String    | Stores user's name           |
| age            | Integer   | Stores user's age            |
| city           | String    | Stores user's city           |
| hobby          | String    | Stores user's hobby          |
| favorite_food  | String    | Stores user's favorite food  |
| favorite_color | String    | Stores user's favorite color |

### Algorithm

1. Store personal information in variables.
2. Ask the user for their favorite food.
3. Ask the user for their favorite color.
4. Check whether the user entered an empty value.
5. Display an error message if the input is empty.
6. Calculate age in months.
7. Display all information in a formatted output.

### Data Structures

This project uses:

* Variables
* Strings
* Integers

No advanced data structures were required for this beginner project.

### Program Architecture

Input → Processing → Output

**Input**

* Favorite food
* Favorite color

**Processing**

* Input validation
* Age conversion from years to months

**Output**

* Formatted display of personal information

---

## Visual Documentation

### User Input

This screenshot shows the program prompting the user to enter their favorite food and favorite color.

![User Input](Screenshots\Screenshot 2026-06-10 135615.png)

---

### Input Validation

This screenshot demonstrates the validation feature. When the user enters an empty value for the favorite color, the program displays an error message and requests valid input.

![Input Validation](Screenshots\Screenshot 2026-06-10 135724.png)

---

### Final Output

This screenshot shows the completed output displaying all personal information, including age in months, city, hobby, favorite food, and favorite color.

![Final Output](Screenshots\Screenshot 2026-06-10 135543.png)

---

## Sample Output

```text
========================================
      PERSONAL INFORMATION MANAGER
========================================

Please tell me about yourself:

Enter your favorite food: biryani
Enter your favorite color: black

==============================
YOUR INFORMATION
==============================

Name  : Ginnikunta Suchitra
Age   : 21 (252 months old)

------------------------------

City  : Hyderabad
Hobby : Cooking

==============================

Favorite Food: biryani
Favorite Color: black

========================================
End of program
========================================
```

---

## Testing Evidence

### Test Case 1

**Input**

Favorite Food: biryani

Favorite Color: black

**Expected Result**

Favorite Food: biryani

Favorite Color: black

**Status:** Passed

---

### Test Case 2

**Input**

Favorite Food: biryani

Favorite Color:

**Expected Result**

Program displays:

```text
Input cannot be empty.
```

and asks the user to enter the value again.

**Status:** Passed

---

### Test Case 3

**Input**

Favorite Food: pizza

Favorite Color: blue

**Expected Result**

Favorite Food: pizza

Favorite Color: blue

**Status:** Passed

---

## Challenges & Solutions

### Challenge

User might enter empty input.

### Solution

Added a basic validation check using an if statement and prompted the user to enter a value again.

### Challenge

Formatting the output nicely.

### Solution

Used f-strings along with separators and headings to create a clean and readable display.

---

## Future Improvements

* Allow users to enter all personal information dynamically.
* Save information to a file.
* Add menu options.
* Add validation for age input.
* Store information for multiple users.

---

## Conclusion

This project helped me understand Python fundamentals such as variables, user input, string formatting, conditional statements, basic validation, and simple calculations. It also provided experience in organizing a project using GitHub and writing professional project documentation.



