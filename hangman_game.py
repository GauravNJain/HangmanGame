#A Very basic Hangman Game

#Importing modules from python library
import random

#A function to greet the user/player
def greet_user(name):
    print(f"Hello {name}, to the Hangman Challenge\n (you get 5 guesses)\n")

#A Welcome message for the game
print("\n===== WELCOME TO THE GAME =====\n")
name=input("Enter your name: ")
greet_user(name)

#Wordlist to pick a random word and print the empty list
wordlist=["Hacker", "bug", "bounty"]
display_word=[]
sec_word=random.choice(wordlist)

for letters in sec_word:
    display_word+="_"

print("Word: ")
print(display_word)
print("\n")

#Variables to use furter to count the number of attempts and to stop the game when all the letters are guessed
attempts=0
max_attempts=5
game_over=False

#The main loop will run until the game_over=True
while not game_over:
    guess=input("Guess the letter: ").lower()

    #Traverse through the string to see if the guessed char is present
    for position in range(len(sec_word)):
        letter=sec_word[position]

        #If found it will replace the "_" from the list to the guessed char
        if letter==guess:
            display_word[position]=guess

    #If the guessed letter is not present no. of attempts will be deducted
    if guess not in sec_word:
        attempts+=1
        guesses_left=max_attempts-attempts
        print(f"\nNumber of guesses left: {guesses_left}")

        #If the no. of wrong attempts exceeds the value of 5 the player will loose (game_over=True)
        if attempts>=max_attempts:
            print("You loose :(")
            game_over=True
        
    print(display_word) #Display the list

    #The following will check if "_" char is present in the display_word list, if its not present that means all the letters are guesses and the player won
    if "_" not in display_word:
        print("\nYou Win!")
        game_over=True