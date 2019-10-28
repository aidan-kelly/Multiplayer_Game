#!/usr/bin/env python3
import random
import player

player1 = player.Player("Bert", 10, 16, 5, 3)
player2 = player.Player("Ernie", 10, 16, 5, 3)

def check_for_winner():
    if player1.health_points <= 0 and player2.health_points > 0:
        return "player2"

    elif player2.health_points <= 0 and player1.health_points > 0:
        return "player1"

    elif player1.health_points <= 0 and player2.health_points <= 0:
        return "draw"

    else:
        return "continue"

def roll_dmg_dice(damage_string):
    dice_options = damage_string.split("d")
    total_roll = 0
    multiplier = int(dice_options[0])
    dice_face = int(dice_options[1])

    for x in range(0, multiplier):
        total_roll += random.randint(1, dice_face)

    return total_roll


def roll_to_hit(attacker, defender, attack_dice):

    critical = False

    dice_roll = random.randint(1, 20)

    if dice_roll == 20:
        critical = True

    dice_roll += attacker.to_hit_bonus
    print(f"{attacker.char_name} rolled {dice_roll}! The defender has an armor class of {defender.armor_class}.")

    if dice_roll >= defender.armor_class or critical == True:
        damage_done = roll_dmg_dice(attack_dice) + attacker.damage_bonus

        if critical:
            damage_done += roll_dmg_dice(attack_dice)

        print(f"The attack hit and did {damage_done} damage to {defender.char_name}!")
        defender.health_points -= damage_done
    else:
        print("The attack missed!")




def game_move(move_choice, attacker, defender):

    #1d10 slashing dmg
    if move_choice == 'sword':
        roll_to_hit(attacker, defender, "1d10")


def game_loop(player1, player2):

    while True:
        p1move = input(f"What attack will {player1.char_name} do? > ")

        if p1move == '1':
            game_move('sword', player1, player2)
        
        p2move = input(f"What attack will {player2.char_name} do? > ")

        if p2move == '1':
            game_move('sword', player2, player1)

        
        

game_loop(player1, player2)
