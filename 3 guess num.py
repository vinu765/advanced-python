import random

def choose_word():
    words = ["apple", "banana", "orange", "grape", "strawberry", "watermelon", "kiwi", "pineapple", "mango", "pear", "peach", "blueberry"]
    return random.choice(words)

def display_word(word, guessed_letters):
    return ''.join([letter if letter in guessed_letters else '_' for letter in word])

def hangman():
    word = choose_word()
    guessed_letters = set()
    attempts = 6

    print("Welcome to Hangman!")
    print("Try to guess the word.")

    while attempts > 0:
        print("\n" + display_word(word, guessed_letters))
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter.")
        elif guess in word:
            guessed_letters.add(guess)
            print("Good guess!")
            if all(letter in guessed_letters for letter in word):
                print("\nCongratulations! You guessed the word:", word)
                break
        else:
            attempts -= 1
            print("Sorry, that letter is not in the word. You have", attempts, "attempt(s) left.")
    else:
        print("You lose! The word was:", word)

if __name__ == "__main__":
    hangman()