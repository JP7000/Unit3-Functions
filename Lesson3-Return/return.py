"""
Lesson 3: Return Values - Practice Exercises
"""
def greet(name):
    return f"Hello {name}"

result = greet("Justin")
print(result)

def square(num):
    return num ** 2
result = square(5)
print(f"5 squared is {result}")
area = square(7)
print(f"Area: {area}")

def get_letter_grade(percentage):
    if percentage >= 90:
        return "A"
    elif percentage >= 80:
        return "B"

result = get_letter_grade(80)
print(result)

# RETURN ENDS THE FUNCTION
# ============================================================================
# Practice 1: Rectangle Area
# ============================================================================

def rect_area(l,w):
    area = l * w
    return area
rect = rect_area(3,5)
print(rect)


# ============================================================================
# Practice 2: Temperature Converter
# ============================================================================
def celcius_to_fahrenheit(celcius):
        return (celcius*9/5)+32

print(f"0C = {celcius_to_fahrenheit(0)}F")


# ============================================================================
# Practice 3: Find Maximum
# ============================================================================

def find_max(num1,num2):
     """Return the large of two numbers"""
     if num1 > num2:
          return num1
     return num2
print(f"Max(3,5) = {find_max(3,5)}")

# ============================================================================
# Practice 4: Is Even?
# ============================================================================

def is_even(number):
    #Return True if number is even, False if odd.
    #Method 1: Direct return (best!)

    return number % 2 == 0



# ============================================================================
# Practice 5: Calculate Tip
# ============================================================================




# ============================================================================
# Challenge 1: Calculate Average
# ============================================================================





# ============================================================================
# Challenge 2: Letter Grade
# ============================================================================
