"""
Lesson 4: Variable Scope - Practice Exercises
"""

# ============================================================================
# Practice 1: Local Variables
# Instructions: Create a function that uses local variables for calculations
# ============================================================================

def calculate_pizza_slices():
    total_slices = 24
    people = 6
    slices_per_person = total_slices / people
    return slices_per_person

result = calculate_pizza_slices()
print(f"Each person gets {result} slices!")
#print(people) 
#NameError: name 'people' is not defined
# Local variables does not exist here 

# ============================================================================
# Practice 2: Global Constants
# Instructions: Create global constants and a function that uses them
# ============================================================================

#Global constants (uppercase naming convention)
TAX_RATE = 0.08
SHIPPING_COST = 5.00

def calculate_tax(price):
    return price * TAX_RATE #Can read global constant

def calculate_total(price):
    tax = calculate_tax(price)
    total = price + tax + SHIPPING_COST # using both constants
    return total

item_price = 50
final_total = calculate_total(item_price)
print(f"Price: ${item_price:.2f}")
print(f"Total: $Total: ${final_total:.2f}")


# ============================================================================
# Practice 3: Parameters Instead of Globals
# Instructions: Rewrite the code to use parameters instead of global variables
# ============================================================================
# Parameters are better to update global variables
# X Bad example - Global Variables
score = 0
def add_points():
    global score
    score += 10
    #Where did this run 
    #Who changed the score
    #Hard to debug

# Good example - Parameters and return
def add_points(score):
    return score + 10
score = 0
score = add_points(score)
#clear what cahnged
#easy to test
#easy to debug

# ============================================================================
# Practice 4: Multiple Functions Sharing Data
# Instructions: Create two functions that work together using parameters/return
# ============================================================================



# ============================================================================
# Challenge 1: Shopping Cart System
# Instructions: Build a complete system using proper scope practices
# ============================================================================



# ============================================================================
# Challenge 2: Game Score Calculator
# Instructions: Calculate game score using constants and functions with proper scope
# ============================================================================