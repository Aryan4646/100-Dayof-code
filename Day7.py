import random

words = ['apple', 'banana', 'cat', 'dog', 'elephant', 'fish', 'giraffe', 'hat']
word = random.choice(words)  # simpler way to get a random word
word_guess = ['_'] * len(word)
total_life = 6
guessed_letters = set()

print("Welcome to Hangman!")
print(" ".join(word_guess))

while total_life > 0:
    if ''.join(word_guess) == word:
        print("You guessed the word correctly! 🎉")
        break

    guess_letter = input("Guess a letter:\n").lower()

    if guess_letter in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.add(guess_letter)

    if guess_letter in word:
        for i in range(len(word)):
            if word[i] == guess_letter:
                word_guess[i] = guess_letter
        print("Correct!")
    else:
        total_life -= 1
        print(f"Incorrect. You have {total_life} lives remaining.")

    print(" ".join(word_guess))

if ''.join(word_guess) != word:
    print(f"You lost! The word was '{word}'.")






