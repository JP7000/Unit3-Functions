def calculate_kd(kills,deaths):
    try:
        return kills/deaths
    except ZeroDivisionError:
        print("Can't calculate kd!")
        return 0

print(calculate_kd(20,5))

def process_donation(amount):
    if amount <= 0:
        raise ValueError("Donation must be positive!")
    print(f"Thanks for ${amount}")

try:
    process_donation(25)
    process_donation(-5)
    print("All donations processed!")
except ValueError as e:
    print(f"Error: {e}")

def create_gamertag(tag):
    if tag == "":
        raise ValueError("Gamertag cannot be empty!")
    if " " in tag:
         raise ValueError("Gamertag cannot have spaces!")
    if len(tag) > 15:
        raise ValueError("Gamertag cannot be longer than 15 characters!") 
    else:
        return tag

try:
    print(create_gamertag("ShadowNinja"))
    print(create_gamertag("has spaces"))
except ValueError as e:
    print(f"Error: {e}")

def split_bill(total_text,people):
    try:
        total = float(total_text)
        each = total/people
        return f"${each:2f} per person"
    except ValueError:
        return "Enter a valid total!"
    except ZeroDivisionError:
        return "Need atleast 1 person!"

print(split_bill("fifty",4))
print(split_bill("20.00",0))
print(split_bill("20.00",4))