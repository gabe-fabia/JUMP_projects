import random
import json
import os

# todo: write the scores to a log file

# First function:
#   - asks how many players there are
def menu_rps():

    menu = input("Please input the number of players (1 or 2)!\n")

    try:
        menu in ('1', '2')
        return int(menu)
        
    except: 
        print("You didn't input 1 or 2! \n")
        menu_rps()

# Second function:
#   - handles one round of rps, accounting for number of players

def rps(players) -> str: # should return game outcome ['p1', 'p2', 'draw']

    p1 = input("Player 1, please select: r, p or s \n")
    while not p1 in ["r", "p", "s"] :
        p1 = input("Player 1, please select: r, p or s \n")

    if players == 2:
        p2 = input("Player 2, please select: r, p or s \n")
        while not p2 in ["r", "p", "s"] :
            p2 = input("Player 2, please select: r, p or s \n")
    
    else:
        p2 = random.choice(["r", "p", "s"])
        print(f"Computer chooses {p2}! \n")

    hands = {"p1": p1, "p2": p2} # here, p1 and p2 can only be in ['r','p','s']

    if {hands["p1"], hands["p2"]}  == {"r", "p"}:
        print("Paper beats rock!")
        if hands["p1"] == "p": return 'p1'
        else: return 'p2'
        

    elif {hands["p1"], hands["p2"]} == {"r", "s"}:
        print("Rock beats scissors!")
        if hands["p1"] == "r": return 'p1'
        else: return 'p2'
        

    elif {hands["p1"], hands["p2"]} == {"p", "s"}:
        print("Scissors beats paper!")
        if hands["p1"] == "s": return 'p1'
        else: return 'p2'
        
    else:
        print("It's a draw!")
        return 'draw'
    
# main function: 
#  - after number of players is selected, can loop over multiple games keeping score

def play_rps():

    players = menu_rps() # 1,2 or a prompt for a valid input 

    p1_score = 0
    p2_score = 0
    draws = 0
    
    p1_bot_score = 0
    bot_score = 0
    bot_draws = 0

    while True:

        game = rps(players)

        if players == 2:
            if game == 'p1':
                print("Player 1 wins!")
                p1_score += 1
            elif game == 'p2':
                print("Player 2 wins!")
                p2_score += 1
            else:
                draws += 1
            
        else:
            if game == 'p1':
                print("Player 1 wins!")
                p1_bot_score += 1
            elif game == 'p2':
                print("Computer wins!")
                bot_score += 1
            else:
                bot_draws += 1
        
        again = input("Play again? (y/n) \n")

        while not again in ('y','n'):
            again = input("Play again? (y/n) \n")
        if again == 'y':
            continue
        else: 
            break

    scores = {
        "p1_score" : p1_score,
        "p2_score" : p2_score,
        "draws" : draws, 
        
        "p1_bot_score" : p1_bot_score,
        "bot_score" : bot_score, 
        "bot_draws" : bot_draws
    }

    if os.path.exists("rps_scores.txt") == False:
        empty_file = open("rps_scores.txt", "w") 
        empty_file.close()

    if os.path.getsize("rps_scores.txt") == 0:
        with open("rps_scores.txt", "w") as score_file :
            score_file.write(json.dumps(scores))
        score_file.close()
    else:
        with open("rps_scores.txt", "r") as score_file :
            data = json.load(score_file) # this will be a python dict

            data["p1_score"] += p1_score
            data["p2_score"] += p2_score
            data["draws"] += draws
            data["p1_bot_score"] += p1_bot_score
            data["bot_score"] += bot_score
            data["bot_draws"] += bot_draws

        score_file.close()

        with open("rps_scores.txt", "w") as score_file :
            score_file.write(json.dumps(data))
        score_file.close()
    
    with open("rps_scores.txt", "r") as score_file:
        print(score_file.read())
            
        




