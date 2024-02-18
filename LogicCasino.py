from random import randint


def calculete_winning(bet_amount, selected_slot, winning_slot):
    if selected_slot == winning_slot:
        return bet_amount * 2
    else:
        return - bet_amount


def generate_winning_slot():
    return randint(1, 10)



