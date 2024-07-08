import random

cardNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

userNumbers = []
computerNumbers = []

def game_start():
    global userNumbers, computerNumbers
    userNumbers = []
    computerNumbers = []
    gameChoice = input("Do you want to play a game of Blackjack? Enter 'y' to start the game. Enter 'n' to exit : ").lower()
    print()
    if gameChoice == "y":
        print(r''' 
        $$$$$$$\  $$\                     $$\                               $$\       
        $$  __$$\ $$ |                    $$ |                              $$ |      
        $$ |  $$ |$$ | $$$$$$\   $$$$$$$\ $$ |  $$\ $$\  $$$$$$\   $$$$$$$\ $$ |  $$\ 
        $$$$$$$\ |$$ | \____$$\ $$  _____|$$ | $$  |\__| \____$$\ $$  _____|$$ | $$  |
        $$  __$$\ $$ | $$$$$$$ |$$ /      $$$$$$  / $$\  $$$$$$$ |$$ /      $$$$$$  / 
        $$ |  $$ |$$ |$$  __$$ |$$ |      $$  _$$<  $$ |$$  __$$ |$$ |      $$  _$$<  
        $$$$$$$  |$$ |\$$$$$$$ |\$$$$$$$\ $$ | \$$\ $$ |\$$$$$$$ |\$$$$$$$\ $$ | \$$\ 
        \_______/ \__| \_______| \_______|\__|  \__|$$ | \_______| \_______|\__|  \__|
                                              $$\   $$ |                              
                                              \$$$$$$  |                              
                                               \______/                               
          ''')

        user_cards1()

        # create a function block by defining appropriate variables
        user_round()

        if userScore >= 21:
            exceededScore()

        else:
            gameContinuation = input("Type 'y' to get another card, type 'n' to pass : ").lower()
            print()

            # roundNumber_user += 1

            while gameContinuation == "y":
                user_cardsx()
                user_round()
                if userScore >= 21:
                    exceededScore()
                    break
                else:
                    gameContinuation = input("Type 'y' to get another card, type 'n' to pass : ").lower()
                    print()

            if gameContinuation == "n":
                exceededScore()

    else:
        print("Sorry to see you go, have a nice day!")


def ace_value(numbers):
    for i in range(len(numbers)):
        if numbers[i] == cardNumbers[0] and sum(numbers) <= 11:
            numbers[i] = 11
    return numbers


# noinspection PyTypeChecker
def user_cards1():
    for x in range(2):
        userNumbers.append(random.choice(cardNumbers))
    for y in range(2):
        computerNumbers.append(random.choice(cardNumbers))

    scores()

def user_cardsx():
    userNumbers.append(random.choice(cardNumbers))
    scores()


def scores():
    global userScore, computerScore
    ace_value(userNumbers)
    userScore = sum(userNumbers)
    ace_value(userNumbers)
    computerScore = sum(computerNumbers)


def user_round():
    print(f"\tYour cards: {userNumbers}, current score: {userScore}")
    print(f"\tComputer's first card: [{computerNumbers[0]}]\n")


def exceededScore():
    print(f"\tYour final hand: {userNumbers}, final score: {userScore}")
    print(f" \tComputer's final hand: {computerNumbers}, final score: {computerScore}\n\n")
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

while True:
    game_start()

# def play_blackjack ():
#
#     if userScore >= 21:
#         exceededScore()
#
#     else:
#         gameContinuation = input("Type 'y' to get another card, type 'n' to pass : ").lower()
#         print()
#
#         # roundNumber_user += 1
#
#         while gameContinuation == "y":
#             user_cardsx()
#             user_round()
#             if userScore >= 21:
#                 exceededScore()
#                 break
#             else:
#                 gameContinuation = input("Type 'y' to get another card, type 'n' to pass : ").lower()
#                 print()
#
#         if gameContinuation == "n":
#             exceededScore()
#
# play_blackjack()
#
#
#