'''
Hangman: Develop a word-guessing game with visual progress
and hints to assist players in guessing the hidden word.
'''

import random
def display_hangman(attempts):
    hangman_stages = [
        '''
        -----
        |   |
        |
        |
        |
        |
        -----
        ''',
        '''
        -----
        |   |
        |   O
        |
        |
        |
        -----
        ''',
        '''
        -----
        |   |
        |   O
        |   |
        |
        |
        -----
        ''',
        '''
        -----
        |   |
        |   O
        |  /|
        |
        |
        -----
        ''',
        '''
        -----
        |   |
        |   O
        |  /|\\
        |
        |
        -----
        ''',
        '''
        -----
        |   |
        |   O
        |  /|\\
        |  /
        |
        -----
        ''',
        '''
        -----
        |   |
        |   O
        |  /|\\
        |  / \\
        |
        -----
        '''
    ]
    return hangman_stages[attempts]
def play_hangman():
    words = ["python", "hangman", "programming", "developer", "challenge"]
    word = random.choice(words)
    guessed_letters = set()
    incorrect_guesses = 0
    max_attempts = 6
    word_display = ['_' for _ in word]
    while incorrect_guesses < max_attempts:
        print(display_hangman(incorrect_guesses))
        print("Word:", ' '.join(word_display))
        print(f"Guessed Letters: {', '.join(sorted(guessed_letters))}")
        print(f"Attempts Remaining: {max_attempts - incorrect_guesses}")     
        guess = input("Guess a letter: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue
        guessed_letters.add(guess)
        if guess in word:
            for index, letter in enumerate(word):
                if letter == guess:
                    word_display[index] = guess
            if '_' not in word_display:
                print("Congratulations! You've guessed the word:", word)
                break
        else:
            incorrect_guesses += 1
            if incorrect_guesses == max_attempts:
                print(display_hangman(incorrect_guesses))
                print("Game Over! The word was:", word)
                break
def main():
    while True:
        play_hangman()
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again not in ['yes', 'y']:
            print("Thanks for playing!")
            break
if __name__ == "__main__":
    main()
