def safe_level_up(xp,hours_studied):
    try:
        return xp // hours_studied
    except ZeroDivisionError:
        print("No grind,no glory!")
        return xp // 10
print(safe_level_up(1000,5)) #returns 200
print(safe_level_up(500,0)) #prints "No grind, no glory!" and returns 50
print(safe_level_up(750,3)) #returns 250

def activate_knowledge_crystal(code):
    try:
        return int(code)
    except ValueError:
        return 1
    finally:
        print("Crystal energy surge")

def join_study_squad(members):
    try:
        count = 0
        for char in members:
            if char == ",":
                count += 1
        if not members:
            return 0
        return count + 1
    except (TypeError):
        return 0
    finally:)
        print("Squad Disbanded :("
print(join_study_squad("Alice"))
   