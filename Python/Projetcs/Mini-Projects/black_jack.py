import random


def randomNumber():
    random_number = random.randint(1, 10)
    return random_number


def main():
    name = input('Player 1, give me your name : ')

    # Starting List
    cards = []  # For Adding the cards
    total = []  # Total of the cards ( for ending the game )
    names = []  # Names

    names.append(name)  # Appeding the first name

    adding_the_cards = 0  # For adding to 21
    player = 0  # For name staff
    sum_of_cards = 0  # Sum of cards

    # Main Loop
    while True:
        rand_num = randomNumber()

        # Correct Choice
        while True:
            choice = input('Want a card? (y/n) : ')

            if (choice != 'y') and (choice != 'n'):
                print('Wrong Choice. Try Again')

            else:
                break

        # Give card to the player
        if choice == 'y':
            cards.append(rand_num)
            print(*cards, sep=', ')
            sum_of_cards += cards[adding_the_cards]
            adding_the_cards += 1

            print(f'Total is {sum_of_cards}')

        # If player won or lost
        if (sum_of_cards > 21) and (player == 0):
            cards.clear()
            return f'I am sorry {names[0]}, you lost'

        elif (sum_of_cards > 21) and (player == 1):
            cards.clear()
            return f'I am sorry {names[1]}, you lost'

        elif (sum_of_cards == 21) and (player == 0):
            return f'{names[0]} you won'

        elif (sum_of_cards == 21) and (player == 1):
            return f'{names[1]} you won'

        # Exiting programm
        if (choice == 'n') and (player == 0):
            total.append(sum_of_cards)
            print(f'You have {sum_of_cards}')
            player = 1
            adding_the_cards = 0
            sum_of_cards = 0
            cards.clear()
            name = input('Player 2, give me your name : ')
            names.append(name)

        elif (choice == 'n') and (player == 1):
            total.append(sum_of_cards)
            # Winning check
            if total[0] > total[1]:
                return f'{names[0]} won'

            elif total[0] == total[1]:
                return 'Equal Game'

            else:
                return f'{names[1]} won'


print(main())
