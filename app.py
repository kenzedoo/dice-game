import random

# GitHub Access Token: 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


authed_players = ["Tom", "Mac", "Seth", "Kyle"] #Array
winner_name = "" #String
players = {} #Map
num_of_games = 5 #Int
total_scores = {} #Map


# function to sign in user
def sign_in():
    username = input("What is your name player: ").capitalize()
    if username in authed_players:
        players[username] = []
        print("%s logged in" % username)
    else:
        print("invalid sign in")
        sign_in()


# function to initialise game for current user
def play_game(current_player):
    print("Do you want to roll {}? (Y/n)".format(current_player))
    player_input = input()
    if player_input.lower() == "y":
        players[current_player].append(roll_dice(current_player))
    else:
        print("Too bad sucker")
        players[current_player].append(roll_dice(current_player))


# function to roll dice for current user
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


# keep looping sign_in function while keys in players map is less than 2
while len(players.keys()) < 2:
    sign_in()

# keep looping games for num_of_games for each player
for game in range(num_of_games):
    print("Starting game: {}".format(game+1))
    for player in players.keys():
        play_game(player)

# build map of total scores for each user
for player in players.keys():
    total_scores[player] = sum(players[player])


# get winning scores
winners = [key for m in [max(total_scores.values())] for key, val in total_scores.items() if val == m]

# if winners are greater than 1 then game was a draw else print winner
if len(winners) > 1:
    print("Its time to d d d d d d d duel")
    duel_scores = 0
    current_player = []
    for player in players.keys():
        current_player.append(player)
        roll = random.randint(1, 6)
        print("{} has rolled {}".format(player, roll))
        if duel_scores != 0:
            if duel_scores == roll:
                print("The game is a draw!")
            elif duel_scores < roll:
                print("The winner is {} with a score of {}".format(player, total_scores[player]))
            else:
                print("The winner is {} with a score of {}".format(current_player[0], total_scores[current_player[0]]))
        duel_scores = roll
else:
    with open("scores.txt", "a") as file:
        print("The winner is {} with a score of {}".format(winners[0], total_scores[winners[0]]))
        file.write("{},{}\n".format(winners[0], total_scores[winners[0]]))
        file.close()
