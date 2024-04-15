import math, time
from tic_tac_toe import alpha_beta_search
from utility import utility



def isterminal(state):
    utility_result = utility(state, n)
    if(utility_result != 'not_terminal'):
        if(utility_result == 1):
            print("you won the game :)")
        elif(utility_result == -1):
            print("you lost the game :(")
        else:
            print("draw :/")
        print("end of the game")
        return True
    return False


def print_state(state):
    print("current state : ", end="")
    for row in state:
        print("\n")
        for value in row:
            if(value == 0):
                print(value, " ", end="")
            elif(value == 1):
                print('X', " ", end="")
            else:
                print('Y', " ", end="")
    print("\n\n")


def getMove():
    move = input("enter next move(row,col) : ")
    separated_move = move.split(',')

    while((separated_move[0].isdigit() == False) 
            or (separated_move[1].isdigit() == False)):
        print("\nyour input is wrong.please try again\n")
        move = input("enter next move(row,col) : ")
        separated_move = move.split(',')

    row = int(separated_move[0])
    col = int(separated_move[1])
    
    return row, col


# driver
n = input("please enter game dimension(between 2 and 10) : ")
if((n.isdigit() == False) or (int(n) < 2) or (int(n) > 10)):
    n = 3
else:
    n = int(n)

state = [[0 for x in range(n)] for y in range((n))]

starter = input("who plays against computer?(user/computer) : ")
difficulty_level = input("\nenter difficulty level(easy/hard) : ")


if(starter == "computer"):

    if(difficulty_level == "easy"):
        depth_limit_2 = 0
        print("\ngame starts at easy difficulty")
    else:
        depth_limit_2 = 4

    depth_limit_1 = 4

    while True:

        print_state(state)

        if(isterminal(state) == True):
            break

        time.sleep(2)
        move = alpha_beta_search(state, n, 'max', depth_limit_1)
        state[move[0]][move[1]] = 1

        print_state(state)

        if(isterminal(state) == True):
            break

        time.sleep(2)
        opponent_move = alpha_beta_search(state, n, 'min', depth_limit_2)
        state[opponent_move[0]][opponent_move[1]] = -1


else:

    if(difficulty_level == "easy"):
        depth_limit = 0
        print("\ngame starts at easy difficulty")
    else:
        depth_limit = 4

    
    while True:

        print_state(state)

        if(isterminal(state) == True):
            break

        row, col = getMove()
        
        while((row >= n) or (row < 0) or (col >= n) 
              or (col < 0) or (state[row][col] != 0)):
            print("\nyour input is wrong.please try again\n")
            row, col = getMove()

        state[row][col] = 1

        print_state(state)

        if(isterminal(state) == True):
            break

        time.sleep(1)
        opponent_move = alpha_beta_search(state, n, 'min', depth_limit)
        state[opponent_move[0]][opponent_move[1]] = -1

