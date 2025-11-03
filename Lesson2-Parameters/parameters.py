def introduce(name, age, grade):
    print(f"This is {name}")
    print(f"{name} is {age} years old.")
    print(f"They are in grade {grade}.")

introduce("Emma",16,11)
#introduce(15, "Sam", 10) wrong code

# addition function

def add_numbers(num1, num2):
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")

add_numbers(10,5)
add_numbers(25,17)

def subtract_numbers(num1, num2):
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")

subtract_numbers(20,8)
subtract_numbers(50,23)

def calculate_percentage(score,max_score):
    percentage = (score / max_score) * 100
    print(f"{score}/{max_score} = {percentage}%")

calculate_percentage(85,100)
calculate_percentage(47,50)
calculate_percentage(18,20)