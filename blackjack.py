import random
from art import logo


def game():
    print(logo)
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    computer_cards = []
    user_cards = []
    gambling = True
    computer_score = 0
    user_score = 0


    def add_card_user(user_cards, user_score):
        user_cards.append(random.choice(cards))
        user_score += user_cards[-1]
        return user_score


    def add_card_computer(computer_cards, computer_score):
        computer_cards.append(random.choice(cards))
        computer_score += computer_cards[-1]
        return computer_score


    def printing_cards():
        print(f"\tYour cards: {user_cards}, current score: {user_score}\n\tComputer's first card: {computer_cards[0]}")


    def final_hand():
        print(f"Your final hand: {user_cards}, final score: {user_score}")
        print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")


    def compare_cards():
        if user_score <= 21 < computer_score:
            print("Opponent went over. You win 😁")
        elif user_score == 21 and computer_score != 21 or computer_score < user_score < 21:
            print("You win 😃")
        elif user_score > 21:
            print("You went over. You lose 😤")
        elif user_score < computer_score <= 21:
            print("You lose 😤")
        else:
            print("Draw 🙃")


    def change_user(user_cards, user_score):
        user_cards.remove(11)
        user_cards.append(1)
        user_score -= 10
        return user_score


    def change_comp(computer_cards, computer_score):
        computer_cards.remove(11)
        computer_cards.append(1)
        computer_score -= 10
        return computer_score


    for x in range(2):
        user_score = add_card_user(user_cards, user_score)
        computer_score = add_card_computer(computer_cards, computer_score)


    printing_cards()

    if user_score != 21 and computer_score != 21:
        choice = input("Type 'y' to get another card, type 'n' to pass: ")
    else:
        gambling = False
        if user_score == 21 and computer_score != 21:
            final_hand()
            print("Win with a Blackjack 😎")
        elif user_score != 21 and computer_score == 21:
            final_hand()
            print("Lose, opponent has Blackjack 😱")
        else:
            final_hand()
            print("You both have Blackjack, draw!")


    while computer_score < 17:
        computer_score = add_card_computer(computer_cards, computer_score)
        if computer_score > 21 and 11 in computer_cards:
            computer_score = change_comp(computer_cards, computer_score)

    while gambling:
        if choice == 'y' and user_score < 21:
            user_score = add_card_user(user_cards, user_score)
            if user_score > 21 and 11 in user_cards:
                user_score = change_user(user_cards, user_score)
            printing_cards()
            if user_score < 21:
                choice = input("Type 'y' to get another card, type 'n' to pass: ")
        else:
            final_hand()
            gambling = False
            compare_cards()

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
    game()