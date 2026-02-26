# Number Guessing Game

# A game where a player has to guess a number from 
# their specified min/max range with a random choosen amount of attempts

# There will be a selected amount of games choosen by a player
# Then a score will be showed at the end

import random

name = input("What\'s your name?\n")
print("\nWelcome " + name + '!')

# Between 1 and 10 rounds
total_games = int(input("\n(1 - 10) How many rounds would you like to play? "))

times_invalid = 0
while (total_games < 1 or total_games > 10):
    times_invalid += 1

    if (times_invalid == 1):
        total_games = int(input("\nPick a number between 1 and 10: ")); 
    else:
        total_games = int(input())

# Display Rules if the user would like to see rules
see_rules = input("\n(y/n) Would you like to see the rules? ").lower()

if see_rules in ["y", "yes"]:
    # Show rules
    print(
"""
RULES
------------------------------------------------------------------------------------------
The game will ask you to create your own MIN and MAX number.

Just make sure that the number has no more than a range of 100 numbers within bounds.
This will the RANGE that you have for EACH OF YOUR GAMES.

Rules for provided attempts:

Numbers shown are included.

With a range of 

1 to 5 numbers, you will have 2 attempts
6 to 10 numbers, you will have 5 attempts
11 to 20 numbers, you will have 8 attempts
21 to 50 numbers, you will have 12 attempts
51 to 80 numbers, you will have 18 attempts
81 to 100 numbers, you will have 25 attempts

For each attempt you will be shown if the golden number is HIGHER OR LOWER...

Note: 

The minimum number you can have is -1000 and highest max can be 1000 
Program will not behave properly if not followed correctly
------------------------------------------------------------------------------------------""")

# Backround rules in regards to score
#  1 - 5   range.  Game lost/won --> -/+ 50pts
#  6 - 10  range.  Game lost/won --> -/+ 75pts
#  11 - 20 range.  Game lost/won --> -/+ 100pts
#  21 - 50 range.  Game lost/won --> -/+ 200pts
#  51 - 80 range.  Game lost/won --> -/+ 300pts
#  81 - 100 range. Game lost/won --> -/+ 400pts

# Function to return an added score to the end of a game
# Outcome refers to whether the player won or lost win = 'win', loss = 'loss'

def add_new_score(range, outcome):
    if ((range >= 1) and (range <= 5)): 
        if (outcome == 'win'): return 50
        else: return -50

    elif ((range >= 6) and (range <= 10)): 
        if (outcome == 'win'): return 75
        else: return -75

    elif ((range >= 11) and (range <= 20)): 
        if (outcome == 'win'): return 100
        else: return -100

    elif ((range >= 21) and (range <= 50)): 
        if (outcome == 'win'): return 200
        else: return -200

    elif ((range >= 51) and (range <= 80)): 
        if (outcome == 'win'): return 300
        else: return -300

    elif ((range >= 81) and (range <= 100)): 
        if (outcome == 'win'): return 400
        else: return -400
    

# Function that calculates range
def find_range(min, max):
    return max - min + 1

# Function that calculates game attempts
def calc_total_attempts(bounds):

    if   ((bounds >= 1) and (bounds <= 5)): return 2
    elif ((bounds >= 6) and (bounds <= 10)): return 3
    elif ((bounds >= 11) and (bounds <= 20)): return 6
    elif ((bounds >= 21) and (bounds <= 50)): return 12
    elif ((bounds >= 51) and (bounds <= 80)): return 15
    elif ((bounds >= 81) and (bounds <= 100)): return 25
    
    # Error return value (Something went wrong)
    return -1

# Function that makes GOLDEN NUMBER
def generate_golden_number(min, max):
    return random.randint(min, max)

seperator = "=========================================="
curr_guess = -1

# This var is used for exception handling to see if the user
# has placed inncorect input before or for the first time
more_than_one = False

# This is the entire score for all the games played
total_score = 0
for game_num in range (1, total_games + 1):
    print("\n" + seperator + "\nGAME " + str(game_num) + '.')

    min = int(input("\nMinimum: "))

    # Exception for min
    while ((min < 0) or (min > 900)):
        min = int(input(' ' * len("Minimum: ")))
    
    max = int(input("Maximum: "))

    # Exceptions for max / range
    while ((max - min + 1 > 100) or (max > 1000) or (min >= max)):
        max = int(input(' ' * len("Minimum: ")))
    
    # Finding the range
    range = find_range(min, max)

    # Select a GOLDEN NUMBER
    gold_number = generate_golden_number(min, max)

    #Finding total attempts
    total_attempts = calc_total_attempts(range)

    if (game_num > 1): more_than_one = False

    # Have the user try and guess that number for a supplied number of attempts
    while ((total_attempts > 0) and (curr_guess != gold_number)):
        curr_guess = int(input("\nGuess: "))

        # Exception to ensure the guess is within proper range

        while ((curr_guess < min) or (curr_guess > max)):

            # First time inccorrect
            if (not more_than_one):
                more_than_one = True
                print("Your number should be between", min, "and", str(max) + '.' + '\n')

                curr_guess = int(input("New Guess: "))
            else:
                curr_guess = int(input("           "))

        
        # Include help to show whether the number is higher or lower
        if (curr_guess < gold_number): print("Higher!")
        else: 
            if (curr_guess != gold_number): print("Lower!")
        
        if (curr_guess != gold_number):
            total_attempts -= 1
    
    # Current game playing is now over 

    # Var to see whether player won/lost
    # If won, value will be 'win', otherwise it will be 'loss'
    result = ''

    # Check to see if user guessed correct number 
    if (curr_guess == gold_number):
        print("Well done. You guessed the correct number!")
        result = 'win'

    else: 
        print("\nGood try, the number was " + str(gold_number))
        result = 'loss'

    # Add to the total score, whether it increases or decreases (+,-)
    total_score += add_new_score(range, result)

    # Added to the end of each game
    print(seperator)

# Finally after all games have been played. Type total score
print("\nYour Total Score is " + str(total_score))

# Placeholder
input()