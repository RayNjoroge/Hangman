import random
from words import words
from hangman_visual import draw_hangman
import string
import sys

def main():
    play_hangman()

def get_valid_word(words):
    """choose a word randomly from list"""
    word = random.choice(words)
    return word.upper()

"""function for game logic"""
def hangman():
    word = get_valid_word(words)
    """var to store set with letters in the word"""
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    """what user has already guessed"""
    used_letters = set()
    
    """lives to determine number of instances a player can play a game before they loose"""
    lives = 7

    """get user input"""
    while len(word_letters) > 0 and lives > 0:
        """
            showing used letters
            # ' '.join(['a', 'b', 'cd']) --> 'a b cd'
        """
        print("")
        print(f"You have {lives} lives left and you have used these letters: ", " ".join(used_letters))
        
        """show the current word - while concealing the missing letters
        (ie W - R D)"""
        word_list = [letter if letter in used_letters else '-' for letter in word]
        draw_hangman(lives)
        print("")
        print("Current word: ", " ".join(word_list), end="")
        print(f" (word has {len(word)} letters)")
        
        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                # take away a life if letter is wrong
                lives = lives - 1
                print(f"Letter {user_letter} is not in the word.")
        elif user_letter in used_letters:
            print("You have already used that letter. Guess another letter!!")
        elif len(user_letter) > 1 or not user_letter.isalpha():
            print("Please enter a single alphabet only!")
        else:
            print("Invalid character. Please Try Again!")

    # gets here when len(word_letters) == 0 OR when == 0
    if lives == 0:
        draw_hangman(lives)
        print("")
        print(f"Game over 😢. Sorry, the word was {word}")
    else:
        print("")
        print(f"Yay!, You guessed the {word} correctly.🎉🎉")

"""Function to play or quit the game"""
def play_hangman():
    print("")
    print("===== Welcome to the Hangman Game =====")
    print("")
    
    """ 
        Conditions to be checked for the func to work
        # if user chooses yes, call function hangman() to play game
        # elif user chooses no, quit game
        # else, prompt user to select valid choice
    """
    while True:
        choice = input("Do you want to play hangman? (yes/ no): ").lower()
        
        if 'yes' in choice:
            hangman()
        elif 'no' in choice:
            print("Quitting the game...")
            sys.exit("...Bye, See you Later!👋👋\n")
        else:
            print("Please enter a valid choice!")
        print("\n")


if __name__ == "__main__":
    main()