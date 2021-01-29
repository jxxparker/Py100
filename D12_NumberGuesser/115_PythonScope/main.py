#global scope

# player_health = 10

# def game():
#   def drink_potions():
#     potion_strength = 2
#     print(player_health)

#   drink_potions()

#there is no block scope

game_level = 3

def create_enemy():
    enemies = ["Skeleton", "Zombie", "Alien"]
    if game_level < 5:
        new_enemy = enemies[0]

    print(new_enemy)

create_enemy()