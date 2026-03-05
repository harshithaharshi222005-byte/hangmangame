import random

# Predefined word list
words = ["python", "java", "computer", "program", "developer"]

# Select random word
chosen_word = random.choice(words)
word_display = ["_"] * len(chosen_word)

attempts = 6
guessed_letters = []

print("🎮 Welcome to Hangman Game!")
print("Guess the word one letter at a time.")

while attempts > 0 and "_" in word_display:
    print("\nWord:", " ".join(word_display))
    print("Attempts left:", attempts)
    
    guess = input("Enter a letter: ").lower()

    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue

    guessed_letters.append(guess)

    if guess in chosen_word:
        print("Correct guess! ✅")
        for i in range(len(chosen_word)):
            if chosen_word[i] == guess:
                word_display[i] = guess
    else:
        print("Wrong guess! ❌")
        attempts -= 1

if "_" not in word_display:
    print("\n🎉 Congratulations! You guessed the word:", chosen_word)
else:
    print("\n😢 You lost! The word was:", chosen_word)