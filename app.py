import random

authed_players = ["Tom", "Mac", "Seth", "Kyle"]
winner_name = ""
players = {}
num_of_games = 5
total_scores = {}


def sign_in():
    username = input("What is your name player: ").capitalize()
    if username in authed_players:
        players[username] = []
        print("%s logged in" % username)
    else:
        print("invalid sign in")
        sign_in()


def play_game(current_player):
    print("Do you want to roll y/n", current_player)
    player_input = input()
    if player_input == "y":
        players[current_player].append(roll_dice(current_player))
    else:
        print("Too bad sucker")
        players[current_player].append(roll_dice(current_player))


def roll_dice(current_player):
    score = 0
    dice_roll1 = random.randint(1, 6)
    dice_roll2 = random.randint(1, 6)
    dice_roll3 = random.randint(1, 6)
    dice_score = dice_roll1 + dice_roll2

    print("Roll1 {} Roll2 {}".format(dice_roll1, dice_roll2))

    if dice_score % 2 == 0:
        score += (dice_score + 10)
        print("+10 points")

    if dice_score % 2 != 0:
        score += (dice_score - 5)
        print("-5 points")
        if dice_score < 0:
            score = 0
            print("Score is negative value, setting to 0")

    if dice_roll1 == dice_roll2:
        score += dice_roll3
        print("Double trouble adding {} to score".format(dice_roll3))

    print("{} has scored: [{}]".format(current_player, score))

    return score


# if x2 > x:
#     print("player 2 wins")
# print(("player 2 total score is: " + str(x2)))
# #
# if x > x2:
#     print("player 1 wins")
# print(("player 1 total score is: " + str(x)))
# if x > x2:
#     score6 = x
#     winner_name = username
# else:
#     score6 = x2
#     winner_name = username2
#
#
# file = open("winnerwinner.txt", "t+a")
# file.write(winner_name)
# file.write(str(score6))
# file.write(",")
# file.close()


# def leader_board():
#     with open("score.txt", "r") as file:
#         scores = file.read()
#         new_scores = scores.split()
#         swapped = True
#         while swapped:
#             swapped = False
#             for i in range(len(new_scores) - 1):
#                 if new_scores[i][-3:-1] < new_scores[i + 1][-3:-1]:
#                     new_scores[i], new_scores[i + 1] = new_scores[i + 1], new_scores[i]
#                     swapped = True
#         if len(new_scores) - 1 < 5:
#             for count in range(len(new_scores)):
#                 print(new_scores[count]),
#         else:
#             for count in range(5):
#                 print(new_scores[count])


while len(players.keys()) < 2:
    sign_in()

for game in range(num_of_games):
    for player in players.keys():
        play_game(player)

for player in players.keys():
    total_scores[player] = sum(players[player])

winners = [key for m in [max(total_scores.values())] for key, val in total_scores.items() if val == m]

if len(winners) > 1:
    print("Its time to d d d d d d d duel")
else:
    print("The winner is {} with a score of {}".format(winners[0], total_scores[winners[0]]))
