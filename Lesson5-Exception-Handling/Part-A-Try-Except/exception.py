"""
Lesson 5: Exception Handling - Practice Exercises
"""
#Common Exception Types

#1-ZeroDivisionError
#print(10/0) # ZeroDivisionError: division by zero

#2-TypeError
#print("5" + 5) #TypeError: unsupported operand type
#type(s) for +: 'int' and 'str'

#3-ValueError
# print(int("5"))
# print(int('bt')) # ValueError: invalid
# literal for int() with base 10: 'bt

#4-NameError
#print(school) #NameError: name 'school' isn't defined
try:
    result = 10/0
except:
    print("Oops! Can't divide by 0.")

# CATCHING SPECIFIC ERROR
try:
    result = 10/0
except ZeroDivisionError:
    print("Oops! Can't divide by 0.")
except ValueError:
    print("That's not a number")

# ==========================
# Practice 1: Safe Division
# Instructions: Create a function that divides two numbers safely
# ==========================
def safe_division(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Warning: Division By Zero!")
        return 0
    except Exception as error:
        print(f"An error occured: {error}")


# ==========================
# Practice 2: Safe Input
# Instructions: Create a function that safely gets an integer from user
# ==========================
def get_age():
    try:
        age = int(input('Enter age:'))
        return age
    except ValueError:
        print('Please enter a number!')
        return 0
user_age = get_age()
print(f"You are {user_age} years old.")
   

# ==========================
# Challenge 1: Safe Calculator
# Instructions: Build a calculator that handles invalid input and division by zero
# ==========================



# ==========================
# Challenge 2: Grade Input Validator
# Instructions: Keep asking for a grade until a valid number between 0-100 is entered
# ==========================
def get_valid_grade():
    try:
        grade = float(input("Enter grade (0-100): "))
        if 0 <= grade <= 100:
            return grade
        else:
            print("Error: Grade must be between 0 and 100!")
    except ValueError:
        print("Error: Please enter a valid number!")
