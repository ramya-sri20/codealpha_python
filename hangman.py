import random

words = ["python", "apple", "banana", "computer", "school"]

word = random.choice(words)
guessed_letters = []
wrong_guesses = 0
max_wrong = 6

print("🎮 Welcome to Hangman!")

while wrong_guesses < max_wrong:
    display = ""

    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "

    print("\nWord:", display)

    if "_" not in display:
        print("🎉 Congratulations! You guessed the word:", word)
        break

    guess = input("Enter a letter: ").lower()

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess not in word:
        wrong_guesses += 1
        print("❌ Wrong guess!")
        print("Remaining chances:", max_wrong - wrong_guesses)

if wrong_guesses == max_wrong:
    print("\n😢 Game Over!")
    print("The word was:", word)