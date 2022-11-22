import random

options = ["ROCK", "PAPER", "SCISSORS"]

print("Enter Rock, Paper or Scissors to play against the computer:")

score = 0
trials = 3

while trials > 0:
    com_choice = random.choice(options)
    player_choice = input(">")
    player_choice = player_choice.upper()

    if player_choice in options:
        if player_choice == com_choice:
            print(f"It's a tie, both selected {player_choice}")
        elif player_choice == "ROCK":
            if com_choice == "SCISSORS":
                score += 2
                print(f"You win :), Rock wins Scissors\n Your score is {score} points")
                
            else:
                trials-=1
                print(f"You lose :(, Paper covers Rock\n {trials} trials left")
        elif player_choice == "PAPER":
            if com_choice == "ROCK":
                score += 2
                print(f"You win :), Paper wins Rock\n Your score is {score} points")
            else:
                trials-=1
                print(f"You lose :(, Scissors cuts Paper\n {trials} trials left")
        elif player_choice == "SCISSORS":
            if com_choice == "PAPER":
                score += 2
                print(f"You win :), Scissors cuts Paper\n Your score is {score} points")
            else:
                trials-=1
                print(f"You lose :(, Rock breaks Scissors\n {trials} trials left")
    else:
        trials-=1
        print(f"You entered a wrong option\n You have {trials} trials left")

print(f"Game Over!!! \nYou're out of trials\n Your final score is {score}")