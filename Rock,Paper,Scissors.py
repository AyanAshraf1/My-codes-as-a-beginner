import os
import random
import time
import tkinter as tkk


def bot():
    global times
    boty = ['Rock', 'Paper', 'Scissors']
    lot = random.choice(boty)
    score = 0
    bot_score = 0
    try:
        times = int(input("How much times do you want to play?: "))
        for i in range(0, times):
            lot = random.choice(boty)
            user = input("Choose between 1)Rock 2)Paper 3) Scissors: ")
            for i in range(3, 0, -1):
                time.sleep(1)
                print(i)
            if user == lot:
                print("Tie")
                print(f"Bot: {lot}, and User(you): {user}")
                score += 1
                bot_score += 1
            elif user == "Rock" and lot == "Scissors":
                print("You won!")
                print(f"Bot: {lot}, and User(you): {user}")
                score += 1
            elif user == "Paper" and lot == "Rock":
                print("You won!")
                print(f"Bot: {lot}, and User(you): {user}")
                score += 1
            elif user == "Scissors" and lot == "Paper":

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
