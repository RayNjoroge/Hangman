
# Hangman Game

A simple game that requires a user to guess letters forming a word that is randomly selected from a <br> list of words.

# Author

Raymond Njoroge

## Description

Upon running the file(hangman.py), there's a welcome message followed by a prompt to choose to play. If the player chooses 'yes', the game starts and if they choose 'no', the dashboard exits.

The player is required to guess letters forming a word that is randomly selected by the program from a list of words.<br>

The player has 7 chances to guess correctly. If they choose a letter in the word, it's filled in with the other letters missing displayed as dashes (i.e W - O R D). Any time the user makes a wrong guess, a hangman visual is drawn depending on the number of lives left. After the instance of every game, the player gets to chose whether to play the game again or quit.

## Requirements
Python3.x ![Static Badge](https://img.shields.io/badge/python-3.x-blue)


## How to Install and Run the Code

1. Ensure you have Python3.x installed on your system.
2. Clone the repository.
3. Open the terminal / command prompt and navigate to the location of the cloned repo.
4. Run the script by executing the following command: python3 hangman.py.
5. Upon running the script, the user is welcomed and prompted to either choose 'yes' to play <br>
    or 'no' to quit the dashboard.
6. Guess the letters to form the word.
7. One gets 7 chances to play.<br> If the player guesses the word correctly, one gets a congratulatory <br>
    message and the actual word is shown. The player is then prompted to choose whether or not to play again.<br>
    If the chances end before getting the word correctly, the game ends, the word is revealed, a hangman figure is <br> revealed and one gets a choice to play again.

## Credits

Please look up the following resources:<br>
    1. freecodecamp's course:- 12 Beginner Python Projects - Coding Course (by Kylie Ying)
        - <https://www.youtube.com/watch?v=8ext9G7xspg&t=2s>
    2. How to Create a Hangman Game Using Python
        - <https://www.makeuseof.com/python-game-hangman-create/?utm_source=flipboard&utm_content=topic%2Fadventuregame>
