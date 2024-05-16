# function to draw hangman visual according to the number of lives

def draw_hangman(lives):
    if lives == 6:
        print("________      ")
        print("|      |      ")
        print("|             ")
        print("|             ")
        print("|             ")
        print("|             ")
    elif lives == 5:
        print("________      ")
        print("|      |      ")
        print("|      0      ")
        print("|             ")
        print("|             ")
        print("|             ")
    elif lives == 4:
        print("________      ")
        print("|      |      ")
        print("|      0      ")
        print("|     /       ")
        print("|             ")
        print("|             ")
    elif lives == 3:
        print("________      ")
        print("|      |      ")
        print("|      0      ")
        print("|     /|      ")
        print("|             ")
        print("|             ")
    elif lives == 2:
        print("________      ")
        print("|      |      ")
        print("|      0      ")
        print("|     /|\\     ")
        print("|             ")
        print("|             ")
    elif lives == 1:
        print("________      ")
        print("|      |      ")
        print("|      0      ")
        print("|     /|\\     ")
        print("|     /       ")
        print("|             ")
    elif lives == 0:
        print("________      ")
        print("|      |      ")
        print("|      0      ")
        print("|     /|\\     ")
        print("|     / \\     ")
        print("|             ")

draw_hangman(lives=7)