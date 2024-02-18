from decouple import config
import LogicCasino

starting_money = int(config('MY_MONEY'))


def play_game():
    money = starting_money

    while True:
        print(f'You have {money}$')
        if money <= 0:
            print(f'You do not have enough funds to continue the game')
            break
        slot = None
        while slot not in range(1, 11):
            try:
                slot = int(input('choose a slot from 1 to 10: '))
                if slot < 1 or slot > 10:
                    print("Strictly from 1 to 10!!!")
            except ValueError:
                print('The selected slot must be a side from 1 to 10')

        bet_amount = int(input(f'how much do you want to bet? '))
        winning_slot = LogicCasino.generate_winning_slot()
        winnings = LogicCasino.calculete_winning(bet_amount, slot, winning_slot)
        if winnings > 0:
            print(f'You win {winnings}$')
            money += winnings
        else:
            print(f'You lost...')
        play_again = input('would you like to play again? "yes." "no.": ').lower()
        if play_again == 'no':
            break
    if money >= starting_money:
        print(f'Congratulations! You have won {money - starting_money}$')
    elif money < starting_money:
        print(f"Unfortunately, you lost {starting_money - money}$.")
    else:
        print('Tie!')


if __name__ == '__main__':
    play_game()
