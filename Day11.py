import random
import blackjack_Art
print(blackjack_Art.art)

def card_deal():
    card_values = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(card_values)

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0  # Blackjack
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(u_score, c_score):
    if u_score == c_score:
        return "Draw"
    elif c_score == 0:
        return "You lost, opponent has blackjack."
    elif u_score == 0:
        return "You won with a Blackjack!"
    elif u_score > 21:
        return "You went over. You lose!"
    elif c_score > 21:
        return "Opponent went over. You win!"
    elif u_score > c_score:
        return "You win!"
    else:
        return "You lose!"

print("Welcome to the Blackjack Game!")

user_cards = []
computer_cards = []
user_score = -1
computer_score = -1
is_game_over = False

for _ in range(2):
    user_cards.append(card_deal())
    computer_cards.append(card_deal())

while not is_game_over:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)

    print(f"Your cards: {user_cards}, current score: {user_score}")
    print(f"Computer's first card: {computer_cards[0]}")

    if user_score == 0 or computer_score == 0 or user_score > 21:
        is_game_over = True
    else:
        user_choice = input("Type 'y' to get another card, type 'n' to pass: ")
        if user_choice == "y":
            user_cards.append(card_deal())
        else:
            is_game_over = True

while computer_score != 0 and computer_score < 17:
    computer_cards.append(card_deal())
    computer_score = calculate_score(computer_cards)

print(f"\nYour final hand: {user_cards}, final score: {user_score}")
print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
print(compare(user_score, computer_score))
