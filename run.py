import random


def game():
    """starts the game, chooses a word randomly from the
    words_to_guess list, checking if users guesses is correct according
    to the word that was choosen"""

    words_to_guess = ["hangman", "computer", "python", "car", "girl", "boy"]
    word = random.choice(words_to_guess)
    chances = 10
    guessdone = ""
    valid_letter = set("abcdefghijklmnopqrstuvwxyz")

    while len(word) > 0:
        main_word = ""
        
        for letter in word:
            if letter in guessdone:
                main_word = main_word + letter
            else:
                main_word = main_word + "_ "    

        if main_word == word:
            print(main_word)
            print("You won!!!")
            break

        print("guess the word", main_word)
        guess = input()

        if guess in valid_letter:
            guessdone = guessdone + guess
        else:
            print("enter valid letter")
            guess = input()

        if guess not in word:
            chances = chances - 1
            if chances == 9:
                print("9 guesses left!!")
                print("--------------")   
            if chances == 8:
                print("8 guesses left!!")
                print("--------------")
                print("       O      ")
            if chances == 7:
                print("7 guesses left!!")
                print("--------------")
                print("       O      ")    
                print("       |      ")
            if chances == 6:
                print("6 guesses left!!")
                print("--------------")
                print("       O      ")    
                print("       |      ")
                print("      /       ")
            if chances == 5:
                print("5 guesses left!!")
                print("--------------")
                print("       O      ")    
                print("       |      ")
                print("      / \     ")
            if chances == 4:
                print("4 guesses left!!")
                print("--------------")
                print("       O      ")    
                print("       |\     ")
                print("      / \     ")   
            if chances == 3:
                print("3 guesses left!!")
                print("--------------")
                print("       O      ")    
                print("      /|\     ")
                print("      / \     ") 
            if chances == 2:
                print("2 guesses left!!")
                print("--------------")
                print("       O  |    ")    
                print("      /|\     ")
                print("      / \     ") 
            if chances == 1:
                print("only 1 guess left! save the hangman!!")
                print("--------------")
                print("       O_|    ")    
                print("      /|\     ")
                print("      / \     ")     
            if chances == 0:
                print("a good man died :(")
                print("game over")

            
print("Welcome", input("ENTER YOUR NAME --> "), "!")
print("Try to guess the word in less than 10 attempts")
print("Good Luck")
game()
