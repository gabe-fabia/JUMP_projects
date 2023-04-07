"""

CMD ARCADE

Task: implement rock paper scissors and tic tac toe (can add more games)
    
    rock paper scissors: user can choose to play against another player, or the computer 
    tic tac toe: game board displated on cmd, boilerplate code provided

Functionality: 

    - MAIN file where users can access a MENU to select a game to play
    - game logic seperated into modules where it can be easily maintained
    - results of the games should be persisted in a log file

Tech Requirements:

    - only the python std library is required
    - app shouldnt crash
    - app should stop only when user selects to exit

Extensions (optional):

    - player's progress available between sessions (save and resume states)
    - implement a gui

    
"""


from rps import *

def main():

    game_lib = {
        1: "Rock, Paper, Scissors"
    }

    while True:
        
        print("""
    Your game library:
        1: Rock, Paper Scissors
        """)

        game_choice = input("""
    What game would you like to play?
    Input the game ID, or type 'q' to quit.
        """)
        
        if game_choice == '1':
            play_rps()
            game_choice = None

        elif game_choice == 'q':
            break

if __name__ == "__main__":
    main()
