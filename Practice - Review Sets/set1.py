#Q1
# JORDAN JUST SCORED 45 POINTS!
# THE CROWD GOES WILD!

# LEILA JUST SCORED 28 POINTS!
# THE CROWD GOES WILD!

#Q2
# EPIC = 1370 + 300
# (whats printed) 1670

#Q3
def gen_name(first, last):
    name = first[0].lower + last.lower
    if len(last) < 5:
        name += "1"
    return name

#Q4

# SUNNY
# COLD

#Q5
def playlist_length(songs, avg_duration):
    total_min = len(songs) * avg_duration
    hours = int(total_min) // 60
    min = int(total_min % 60)
    return f"{hours}h {min}m"

#Q6

#Total XP: 220

#Q7

def battle_cry(hero, wpn, dmg):
    return f"{hero.upper()} dwings {wpn.upper()} for {dmg} damage! "