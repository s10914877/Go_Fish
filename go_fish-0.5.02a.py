# Go Fish by Ryan K. - ICT-3
# Version 0.5.02a - Published 11/07/2016


from random import shuffle # Import the SHUFFLE function from the RANDOM library. 
from time import sleep # Use the SLEEP function from the TIME library.
# It is good practice to put ALL of your FROM X IMPORT Y statements at the top of your code.

# I am defining all of the functions my program needs first.  I am defining them in the order which they are used in the game.
# Finally, I have one main go_fish() function that calls all of the other functions I am writing. 


def new_player():   # This function sets the game up for a single human player and handles the rules. 
    print("Welcome to Go Fish-bot Version 0.5.02a.\nI am the premier Go Fish program in the universe.\n")
    user = input("Hello!  What is your name? [Type your name and press enter.]\n")
    print("Hello,", user, "today we are going to play Go Fish!\n")
    # These lines introduce the user to our program and records their name.
    
    rules = int(input("Do you know how to play Go Fish? Enter 0 for NO and 1 for YES.\n"))
    if rules == 0: 
        print("The rules can be found here: http://www.bicyclecards.com/how-to-play/go-fish/\n")
        print("The Deal\n")
        sleep(2) # This line will introduce a pause of (x) seconds.  Gives the user time to read the instructions. 
    else:
        print("Ahh, an expert!  I hope you are more challenging than the last victim, err, player.\n") 
    return user

def make_deck():   # This fucntion will create a brand new deck and shuffle it. 
    deck = ["a Two", "a Three", "a Four", "a Five", "a Six", "a Seven", "an Eight", "a Nine", "a Ten", "a Jack", "a Queen", "a King", "an Ace"]
    full_deck = deck * 4
    print("Ta-Da!  It's a new deck.\n")
    print (full_deck,"\n")
    shuffle(full_deck)
    print("Shuffling...please hold.  This is extremely precise.\n")
    sleep(5)
    print("The deck has been sufficiently randomized.\n")
    print (full_deck,"\n") # REMOVE FROM FINAL CODE. 
    return full_deck

def goes_first():   # This function will determine which player will start the game. 
    user = new_player()
    # Call our new_player()
    deal1 = []
    deal2 = []
    deal3 = []
    deal4 = []
    # Create four emtpy list variables to store the card that is dealt.
    fresh_deck = make_deck()
    value = {"a Two":2, "a Three":3, "a Four":4, "a Five":5, "a Six":6, "a Seven":7, "an Eight":8, "a Nine":9, "a Ten":10, "a Jack":11, "a Queen":12, "a King":13, "an Ace":14}
    # Create a key to have our neccesary values.  CREDIT TO CONNOR FOR THIS IDEA!
    # Need to fix function code.  full_deck variable is NOT being passed to goes_first() function.
    
    deal1 = fresh_deck[0]
    fresh_deck.remove(fresh_deck[0])
    deal2 = fresh_deck[0]
    fresh_deck.remove(fresh_deck[0])
    deal3 = fresh_deck[0]
    fresh_deck.remove(fresh_deck[0])
    deal4 = fresh_deck[0]
    fresh_deck.remove(fresh_deck[0])
    # The above lines make the deal1 through deal4 equal to the top card of the deck.  Then that top card is removed each time.
    print(user, " was dealt",deal1,".\n")
    print("Player 2 was dealt",deal2,".\n")
    print("Player 3 was dealt",deal3,".\n")
    print("Player 4 was dealt",deal4,".\n")
    lowest = min(value[deal1], value[deal2], value[deal3], value[deal4])
    print (lowest) # REMOVE FROM FINAL VERSION. 
    if value[deal1] == lowest:
        print(user, " will play first!\n")
        first_player = 1
    elif value[deal2] == lowest:
        print("Player 2 will play first!\n")
        first_player = 2
    elif value[deal3] == lowest:
        print("Player 3 will play first!\n")
        first_player = 3
    else:
        print("Player 4 will play first!\n")
        first_player = 4
    

def go_fish(): # This is the main go_fish function.  It calls all of the required functions for the game.
    goes_first()

go_fish() # Call go_fish() to play the game, hopefully! 
