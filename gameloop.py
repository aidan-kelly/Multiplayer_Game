#!/usr/bin/env python3
import random
import player

###
###TODO need to add some randomization about who goes first
###

player1 = player.Player("Bert", 35, 16, 5, 3)
player2 = player.Player("Ernie", 35, 16, 5, 3)

#func to determine who was the winner
def check_for_winner():
    if player1.health_points <= 0 and player2.health_points > 0:
        return "player2"

    elif player2.health_points <= 0 and player1.health_points > 0:
        return "player1"

    elif player1.health_points <= 0 and player2.health_points <= 0:
        return "draw"

    else:
        return "continue"

#func to see if the game is over
def check_if_over():
    if player1.health_points <= 0 or player2.health_points <= 0:
        return True
    else:
        return False

#func to roll dice. Input is a string containing:
#[amount of dice]'d'[max roll of that dice]
#eg. 1d12 means we roll a dice with 12 sides, once
def roll_dmg_dice(damage_string):
    dice_options = damage_string.split("d")
    total_roll = 0
    multiplier = int(dice_options[0])
    dice_face = int(dice_options[1])

    for x in range(0, multiplier):
        total_roll += random.randint(1, dice_face)

    return total_roll

#we see if a player hits, if they do we roll damage as well
def roll_to_hit(attacker, defender, attack_dice):

    critical = False
    dice_roll = random.randint(1, 20)

    if dice_roll == 20:
        critical = True

    dice_roll += attacker.to_hit_bonus
    print(f"\n{attacker.char_name} rolled {dice_roll}! The defender has an armor class of {defender.armor_class}.")

    if dice_roll >= defender.armor_class or critical == True:
        damage_done = roll_dmg_dice(attack_dice) + attacker.damage_bonus

        if critical:
            damage_done += roll_dmg_dice(attack_dice)

        defender.health_points -= damage_done
        print(f"The attack hit and did {damage_done} damage to {defender.char_name}!\n{defender.char_name} now has {defender.health_points} hp remaining!\n")
        
    else:
        print("The attack missed!\n")



#func will hold all player options
def game_move(move_choice, attacker, defender):

    #1d10 slashing dmg
    if move_choice == 'sword':
        roll_to_hit(attacker, defender, "1d10")


#basic game loop 
def game_loop(player1, player2):

    while True:
        p1move = input(f"What attack will {player1.char_name} do? > ")

        if p1move == '1':
            game_move('sword', player1, player2)

        if check_if_over():
            break
        
        p2move = input(f"What attack will {player2.char_name} do? > ")

        if p2move == '1':
            game_move('sword', player2, player1)

        if check_if_over():
            break

    print(check_for_winner())

        
        

game_loop(player1, player2)
