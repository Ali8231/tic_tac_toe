
# maximizer move is 1
# minimizer move is -1

def utility(state):

    for row in range(3):
        if((state[row][0] == 1) and (state[row][1] == 1) and (state[row][2] == 1)):
            return 1
        elif((state[row][0] == -1) and (state[row][1] == -1) and (state[row][2] == -1)):
            return -1
        
    for col in range(3):
        if((state[0][col] == 1) and (state[1][col] == 1) and (state[2][col] == 1)):
            return 1
        elif((state[0][col] == -1) and (state[1][col] == -1) and (state[2][col] == -1)):
            return -1
        
    if((state[0][0] == 1) and (state[1][1] == 1) and (state[2][2] == 1)):
        return 1
    elif((state[0][0] == -1) and (state[1][1] == -1) and (state[2][2] == -1)):
        return -1

    if((state[0][2] == 1) and (state[1][1] == 1) and (state[2][0] == 1)):
        return 1
    elif((state[0][2] == -1) and (state[1][1] == -1) and (state[2][0] == -1)):
        return -1
        


    terminal_flag = 1

    for row in state:
        for value in row:
            if(value == 0):
                terminal_flag = 0
                
    if(terminal_flag == 1):
        return 0
    else:
        return 'not_terminal'
        


# state = [[1, 1, 1],
#          [1, -1, 1],
#          [-1, 1, -1]]


# print(utility(state))
        

