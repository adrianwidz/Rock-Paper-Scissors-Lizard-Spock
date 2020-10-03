import random

scores = open("rating.txt", "r")
player = input("Enter your name: ")
print("Hello, " + player)
player_score = 0

for score in scores:
    score = score.split(" ")
    if score[0] == player:
        player_score = int(score[1])

scores.close()

options = ["rock", "paper", "scissors"]
different_options = input()
if different_options != "":
    options = different_options.split(",")
print("Okay, let's start")

while True:

    move = input()
    if move == "!exit":
        print("Bye!")
        break

    if move == "!rating":
        print("Your rating: " + str(player_score))
        continue

    if move not in options:
        print("Invalid input")
        continue

    win_or_lose_options = options[options.index(move) + 1::] + options[:options.index(move):]
    split_point = int(len(win_or_lose_options) / 2)
    win_options = win_or_lose_options[split_point::]
    lose_options = win_or_lose_options[:split_point:]

    option = random.choice(options)
    if move == option:
        print("There is a draw (" + option + ")")
        player_score += 50
    elif option in win_options:
        print("Well done. The computer chose " + option + " and failed")
        player_score += 100
    elif option in lose_options:
        print("Sorry, but the computer chose " + option)
