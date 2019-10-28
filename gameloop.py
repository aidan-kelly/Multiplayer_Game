#!/usr/bin/env python3
import random

player1_hp = 35
player2_hp = 35

player1_ac = 16
player2_ac = 16

player1_atk_mod = 5
player2_atk_mod = 5

def roll_dmg_dice(damage_string):
    dice_options = damage_string.split("d")
    total_roll = 0

    if len(dice_options) > 1:
        for x in range(0, dice_options[0]):
            total_roll += random.randint(1, dice_options[1])

    else:
        total_roll += random.randint(1, dice_options[1])

    return total_roll


def roll_to_hit(attacker_mod, defender_ac, attacker_dice, attacker_dmg_bonus):

    dice_roll = random.randint(1, 20)
    dice_roll += attacker_mod

    if dice_roll >= defender_ac:
        damage_done = roll_dmg_dice(attacker_dice) + attacker_dmg_bonus
        print(f"The attack hit and did {damage_done} damage!")
    else:
        print("The attack missed!")
    print(dice_roll)




def game_move(move_choice):

    #1d10 slashing dmg
    if move_choice == 'sword':
        roll_to_hit()


#def game_loop():


    # while True:
