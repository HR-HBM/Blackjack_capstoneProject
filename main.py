import random
from image import logo
cardNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
userCards = []
computerCards = []



def add_card_to_computer():
    while sum(computerCards) < 17:
        computerCards.append(random.choice(cardNumbers))
    calculate_score()

def set_ace_value(numbers):
    for i in range(len(numbers)):
        if numbers[i] == 1 and sum(numbers) <= 11:
            numbers[i] = 11
    if all(number == 1 for number in numbers[:2]):
        numbers[0] = 11
        numbers[1] = 1

def serve_cards():
    for x in range(2):
        userCards.append(random.choice(cardNumbers))
    for y in range(2):
        computerCards.append(random.choice(cardNumbers))

    calculate_score()

def add_card_to_user():
    userCards.append(random.choice(cardNumbers))
    calculate_score()

def calculate_score():
    global userScore, computerScore
    set_ace_value(userCards)
    userScore = sum(userCards)
    set_ace_value(computerCards)
    computerScore = sum(computerCards)

def print_scores():
    print(f"\tYour cards: {userCards}, current score: {userScore}")
    print(f"\tComputer's first card: [{computerCards[0]}]\n")

def finalize_scores():
    print(f"\tYour final hand: {userCards}, final score: {userScore}")
    print(f" \tComputer's final hand: {computerCards}, final score: {computerScore}\n\n")
    if userScore == computerScore:
        print("It's a Draw!")
    elif computerScore < userScore > 21:
        print("You went over, the computer Wins!")

    elif userScore == 21:
        if userScore == computerScore:
            print("It's a Draw!")
        else:
            print("You win!")
    else:
        if computerScore > 21:
            print("the computer went over, you win!")
        elif computerScore < userScore:
            print("You Win!")
        elif computerScore > userScore:
            print("The Computer wins!")

def start_game():
    global userCards, computerCards
    userCards = []
    computerCards = []

    userChoice = input("Do you want to play a game of Blackjack? Enter 'y' to start the game. Enter 'n' to exit : ").lower()
    print()

    if userChoice == "n":
        print("Sorry to see you go. Have a nice day!")
        return False

    elif userChoice == "y":
        print(logo)

        serve_cards()
        print_scores()

        if userScore >= 21:
            finalize_scores()

        else:
            while True:
                gameContinuation = input("Type 'y' to get another card, type 'n' to pass : ").lower()
                print()

                if gameContinuation == "y":
                    add_card_to_user()
                    print_scores()
                    if userScore >= 21:
                        finalize_scores()
                        break

                elif gameContinuation == "n":
                    add_card_to_computer()
                    finalize_scores()
                    break
                else:
                    print("Invalid Entry!")

    else:
        print("Invalid Entry!")

    return True



while True:
   if not start_game():
       break
