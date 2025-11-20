def safe_multiply(x,y):
    try:
        result = x * y
        return result
    except TypeError:
        return 0
print(safe_multiply(5,3))
print(safe_multiply(4,"a"))