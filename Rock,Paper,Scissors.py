import os
import random
import time



def bot():
    global times
    boty = ['rock', 'paper', 'scissors']
    lot = random.choice(boty)
    score = 0
    bot_score = 0
    try:
        times = int(input("How much times do you want to play?: "))
        for i in range(0, times):
            lot = random.choice(boty)
            user = None
            while user not in boty:
                user = input("Choose between 1)rock 2)paper 3) scissors: ").lower()
            for i in range(3, 0, -1):
                time.sleep(1)
                print(i)
            if user == lot:
                print("Tie")
                print(f"Bot: {lot}, and User(you): {user}")
                score += 1
                bot_score += 1
            elif user == "rock" and lot == "scissors":
                print("You won!")
                print(f"Bot: {lot}, and User(you): {user}")
                score += 1
            elif user == "paper" and lot == "rock":
                print("You won!")
                print(f"Bot: {lot}, and User(you): {user}")
                score += 1
            elif user == "scissors" and lot == "paper":

                print("You won!")
                print(f"Bot: {lot}, and User(you): {user}")
                score += 1
            else:
                print("You lose!")
                bot_score += 1
                print(f"Bot: {lot}, and User(you): {user}")

    except ValueError:
        print("Error only enter a number..")
    try:
        print("Analysis: ")
        print(f"Player score: {score}/{times}")
        print(f"Bot score: {bot_score}/{times}")
    except NameError:
        print("..")


bot()


def play_again():
    response = input("Do you want to play again (Y/N): ").upper()
    if response == "Y":
        return True
    else:
        return False
while play_again():
    new_game()
print("Bye Have a nice day.")
