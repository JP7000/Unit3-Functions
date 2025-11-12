#Solution 1
# "FINAL SCORE: 1500"

#Solution 2
"FIRE"
"COLD"

#Solution 3
def generate_hashtag(phrase):
    titled = phrase.title()
    no_spaces = titled.replace(" ", "")
    hashtag = "#" + no_spaces
    if len(hashtag) > 20:
        return "TOO LONG"
    return hashtag

#Solution 4
# "GOAL SMASHED!"

#Solution 5
def battle_cry(hero, wpn, dmg):
    msg = f"{hero.upper()} swings {wpn.upper()} for {dmg} damage!"
    if dmg > 80:
        msg += "CRITICAL HIT!"
        return msg
    
#Solution 6
"AI feels excited!"