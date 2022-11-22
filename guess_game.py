"""
Build a guess game where users tries to guess the number that the computer will select from a given random number set.

If the user gets the number correctly, he/she gets 2 points and an added trial.

Ff he/she misses the number, he loses a trial.

The user has 3 trials at the beginning of the game.
"""

import random

numbers = [random.choice(range(100)) for i in range(6)] 

com_choice = random.choice(numbers)

print("Guess the number selected by the computer from:", numbers)

score = 0
trials = 3

while trials > 0:
    com_choice = random.choice(numbers)
    user_choice = int(input(">"))
    if user_choice in numbers:
        if com_choice == user_choice:
            score += 2
            print(f"You win!\n You have an extra trial and your current score is {score}")
        else:
            print(f"Computer selected: {com_choice}")
            trials-=1
            print(f"You lose \n {trials} trials left")
    else:
        trials -= 1
        print(f"Invalid number selected\n {trials} trials left")

print ("Game Over!")
print(f"Your total score is {score}")




