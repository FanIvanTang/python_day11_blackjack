############### Blackjack Project #####################

# Difficulty Normal 😎: Use all Hints below to complete the project.
# Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
# Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
# Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

# Hint 1: Go to this website and try out the Blackjack game:
#   https://games.washingtonpost.com/games/blackjack/
# Then try out the completed Blackjack project here:
#   http://blackjack-final.appbrewery.repl.run

# Hint 2: Read this breakdown of program requirements:
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
# Then try to create your own flowchart for the program.

# Hint 3: Download and read this flow chart I've created:
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

# Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
# 11 is the Ace.
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
# user_cards = []
# computer_cards = []

# Hint 6: Create a function called calculate_score() that takes a List of cards as input
# and returns the score.
# Look up the sum() function to help you do this.

# Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

# Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

# Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

# Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

# Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

# Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

# Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

# Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.

from art import logo
import random

deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def calculate_score(hand_of_cards):
    """
    take a list of cards (number), and return the score of this hand
    Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10)
    and return 0 instead of the actual score. 0 will represent a blackjack in our game
    check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1.
    You might need to look up append() and remove().
    """

    if len(hand_of_cards) == 2 and (11 in hand_of_cards) and (10 in hand_of_cards):
        # check for a blackjack (a hand with only 2 cards: ace + 10)
        return 0

    while sum(hand_of_cards) > 21 and (11 in hand_of_cards):
        hand_of_cards.remove(11)
        hand_of_cards.append(1)

    return sum(hand_of_cards)


def deal_card():
    return random.choice(deck)


def compare(computer_score, user_score):
    """
    pass in the user_score and computer_score.
    If the computer and user both have the same score, then it's a draw.
    If the computer has a blackjack (0), then the user loses.
    If the user has a blackjack (0), then the user wins.
    If the user_score is over 21, then the user loses.
    If the computer_score is over 21, then the computer loses.
    If none of the above, then the player with the highest score wins.
    """
    if computer_score == user_score and user_score < 22:
        return "You have same score with component, draw"
    if computer_score == 0:
        return "Component is Blackjack! You lose:("
    if user_score == 0:
        return "You are Blackjack! You win :)"
    if user_score > 21:
        return "You went over. You lose:("
    if computer_score > 21:
        return "Component went over. You win :)"
    if user_score > computer_score:
        return "Your score is higher than component. You win :)"
    else:
        return "Your socre is less than component. You lose :("


def if_start_game():
    """
    ask user whether start game, return True or False
    """
    start_game = input("Do you want to play a game of Blackjack? Tpye 'y' or 'n': ")

    while start_game.lower() not in ["y", "n"]:

        start_game = input(
            "opoos, wrong input, Tpye 'y' for start game or 'n' for quit: "
        )

    return start_game == "y"


def get_another_card_or_pass():
    """
    ask user whether get another card, 'y' for get another card, 'n' for pass, and return True or False
    """

    is_continue = input("Type 'y' to get another card, type 'n' to pass: ")

    while is_continue.lower() not in ["y", "n"]:

        is_continue = input(
            "opoos, wrong input, Type 'y' to get another card, type 'n' to pass: "
        )

    return is_continue == "y"


def check_result(computer_hand, user_hand):
    """
    take computer cards and user cards and compare and print out the game result

    """

    c_score = calculate_score(computer_hand)
    u_score = calculate_score(user_hand)

    result = compare(user_score=u_score, computer_score=c_score)

    print(f"  Your final hands: {user_hand}, final score: {u_score}")
    print(f"  Computer's final hands: {computer_hand}, final score: {c_score}")
    print(result)


if __name__ == "__main__":

    ready_start_game = if_start_game()

    while ready_start_game:

        print(logo)

        user_cards = [deal_card(), deal_card()]
        computer_cards = [deal_card(), deal_card()]

        print(f"Your cards: {user_cards}, current score: {calculate_score(user_cards)}")

        first_computer_card = computer_cards[0]
        # this line should be comments after debug
        # print(
        #     f"Computor cards: {computer_cards}, current score: {calculate_score(computer_cards)}"
        # )

        print(f"Computer's first card: {first_computer_card}")

        is_get_another_card = get_another_card_or_pass()

        while is_get_another_card:

            # if calculate_score(computer_cards) < 17:
            #     computer_cards.append(deal_card())

            user_cards.append(deal_card())

            if calculate_score(user_cards) > 21:

                break

            else:

                print(
                    f"Your cards: {user_cards}, current score: {calculate_score(user_cards)}"
                )

                # this line should be comments after debug
                # print(
                #     f"Computor cards: {computer_cards}, current score: {calculate_score(computer_cards)}"
                # )

                print(f"Computer's first card: {first_computer_card}")

                is_get_another_card = get_another_card_or_pass()

        while calculate_score(computer_cards) < 17:
            computer_cards.append(deal_card())

        check_result(user_hand=user_cards, computer_hand=computer_cards)

        ready_start_game = if_start_game()
