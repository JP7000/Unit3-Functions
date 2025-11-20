#Question 1
def safe_multiply(x,y):
    try:
        return x * y
    except TypeError:
        return 0

#Question 2
# print(result) prints -1

#Question 3
def is_positive(value):
    try:
        return isinstance(value, int) and value > 0
    except:
        return False
print(is_positive(-3))

#Question 4
"Processing complete"
"0"

#Question 5
def format_message(code,text):
    try:
        return f"[{code}] {text}"
    except isinstance(code,str,None,bool,float):
        return "[ERROR] invalid"
print(format_message(None, "test"))

#Question 6
# "Calculation done"
# "16"

#Question 7
def safe_average(a,b):
    try:
        return (a+b)/2
    except ZeroDivisionError:
        return 0

#Question 8

"Process complete"
"50.0"

#Question 9

"0"