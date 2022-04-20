"""
Day 12 - Beginner - Scope & Number Guessing Game
"""
#---------------------- Scope ----------------------#

enemies = 1

def increase_enemies():
  enemies = 2
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

# Local Scope 

def drink_potion_1():
    potion_strength = 2
    print(potion_strength)

drink_potion_1()
# can't find potion_strength
# print(potion_strength)


# Global Scope 
player_health=10
def drink_potion_2():
    potion_strength = 2
    print(potion_strength)
    print(player_health)

drink_potion_2()

# NameSpace
# Global Scope 
player_health=10
def game():
    def drink_potion():
        potion_strength = 2
        player_health=1
        print(potion_strength)
        print(player_health)

    # need to call drink_potion() here
    drink_potion()

# now cant find drink_potion()
drink_potion()
