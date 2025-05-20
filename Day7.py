import random
import list_hangman_Day_7
import hangman_Ascii

print("Welcome to Hangman!\n")
random_word = random.choice(list_hangman_Day_7.hangman_words)
guess_word = ["_"] * len(random_word)
lives = 8
guessed_letters = []

print(f"You need to guess the word of length {len(random_word)}: {''.join(guess_word)}")

while lives > 0:
    letter = input("Guess a letter: ").lower()

    if letter in guessed_letters:
        print(f"You already guessed the letter: {letter}")
        continue

    guessed_letters.append(letter)

    if letter in random_word:
        for i in range(len(random_word)):
            if random_word[i] == letter:
                guess_word[i] = letter
        print("Correct guess!")
    else:
        lives -= 1
        print(f"Wrong guess. Lives remaining: {lives}")
        print(hangman_Ascii.hangman_stages[7 - lives])

    print(" ".join(guess_word))

    if ''.join(guess_word) == random_word:
        print("Congratulations! You guessed the word.")
        break
else:
    print(f"You lost! The correct word was: {random_word}")







