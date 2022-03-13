######################## Scope ########################

# enemies = 1
#
# def increase_enemies():
#     enemies = 2
#     print(f"Enemies Inside Function: {enemies}")
#
# increase_enemies()
# print(f"Enemies outside function: {enemies}")
#
# # Local Scope
#
# def drink_potion():
#     potion_strength = 2
#     print(f"Potion Strength: {potion_strength}")
#
# drink_potion()
# # potion_strength will not work because it is only available in drink_potion function
# # print(potion_strength)
#
# # Global Scope
# player_health = 10
#
# def game():
#     def drink_potion_global():
#         potion_strength = 2
#         print(f"Players Health: {player_health}")
#
#     drink_potion_global()
#
# # There is no Block Scope
#
# game_level = 3
#
# def create_enemy():
#     enemies = ["Skeleton", "Zombie", "Alien"]
#     if game_level < 5:
#         new_enemy = enemies[0]
#
#     print(new_enemy)


# Modifying Global Scope

enemies = 1

def increase_enemies():
    print(f"Enemies Inside Function: {enemies}")
    return enemies + 1

enemies = increase_enemies()
print(f"Enemies outside function: {enemies}")


# Global Constants
# Convention to CAPITALIZE_WITH_UNDERSCORES but they can still be modified

PI = 3.14159
URL = "https://www.google.com"
