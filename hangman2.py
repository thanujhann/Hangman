import random
import string
import time

hangman_pics = ["  +---+\n  |   |\n      |\n      |\n      |\n      |\n=========", 

        "  +---+\n  |   |\n  O   |\n      |\n      |\n      |\n=========",

        "  +---+\n  |   |\n  O   |\n  |   |\n      |\n      |\n=========",

        "  +---+\n  |   |\n  O   |\n /|   |\n      |\n      |\n=========", 

        "  +---+\n  |   |\n  O   |\n /|\  |\n      |\n      |\n=========",

        "  +---+\n  |   |\n  O   |\n /|\  |\n /    |\n      |\n=========",

        "  +---+\n  |   |\n  O   |\n /|\  |\n / \  |\n      |\n========="] 


word_bank = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
         'coyote crow deer dog donkey duck eagle ferret fox frog goat '
         'goose hawk lion lizard llama mole monkey moose mouse mule newt '
         'otter owl panda parrot pigeon python rabbit ram rat raven '
         'rhino salmon seal shark sheep skunk sloth snake spider '
         'stork swan tiger toad trout turkey turtle weasel whale wolf '
         'wombat zebra ').split()


#while True:
    
print("Welcome to hangman!")
print("Loading word...")
time.sleep(2)
chosen_word = random.choice(word_bank)

size = len(chosen_word)
#print(chosen_word)

#guess = "_"
#guess = guess* size
#print(guess)
guess = "_" *(size)
guesses = 0
attempts = 7
while (attempts != 0 or "_" not in guess):

    user = input("Enter your guess big dawg: ")
    
    
    if(len(user) > 1):
        print("Error! Only one letter")
        
    elif(len(user) == 0):
        print("Error! That aint a letter")
        
    elif(user not in chosen_word):
        attempts -= 1
        print(hangman_pics[guesses], "You have ", attempts ," attempts left") 
        guesses += 1    
        print(guess)
    
    elif(user in guess):
        print("You've already guessed that letter mate")
    
    else:
        for x in range(size):
            if user in chosen_word[x]:
                guess = guess[:x] + user + guess[x+1:]
                print(guess)
           
    if ("_" not in guess):
        break        
    elif(attempts == 0):
        print("MWAHAHAHAHAH YOU LOSE")
                
        
    #print(guess)

print("The word was " + chosen_word)

if ("_" not in guess):
    print("Congratulations! You found the word LETS GOOOO.")


    
