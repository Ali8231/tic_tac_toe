
# maximizer move is 1
# minimizer move is -1


# utility function includes flags for checking
# rows, columns and diagonals for both maximizer
# and minimizer. at first all flags are set to 1.
# if at any time it is determined that a row, column
# or diagonal can not represent a certain terminal condition,
# the corresponding flag is set to 0. it returns 1 for
# maximizer win, -1 for minimizer win and 0 if the board 
# is full


def utility(state, n):

    full_flag = 1

    max_main_diagonal_flag = 1
    min_main_diagonal_flag = 1

    max_secondary_diagonal_flag = 1
    min_secondary_diagonal_flag = 1

    for row in range(n):
        max_row_flag = 1
        min_row_flag = 1

        max_col_flag = 1
        min_col_flag = 1

        for col in range(n):

            if(state[row][col] == 0):
                full_flag = 0 

            if(state[row][col] != 1):
                max_row_flag = 0
            if(state[row][col] != -1):
                min_row_flag = 0

            if(state[col][row] != 1):
                max_col_flag = 0
            if(state[col][row] != -1):
                min_col_flag = 0

            if((row == col) and (state[row][col] != 1)):
                max_main_diagonal_flag = 0
            if((row == col) and (state[row][col] != -1)):
                min_main_diagonal_flag = 0

            if((row + col == n-1) and (state[row][col] != 1)):
                max_secondary_diagonal_flag = 0
            if((row + col == n-1) and (state[row][col] != -1)):
                min_secondary_diagonal_flag = 0


        if(max_row_flag == 1):
            return 1
        elif(min_row_flag == 1):
            return -1
        
        if(max_col_flag == 1):
            return 1
        elif(min_col_flag == 1):
            return -1
        
    if(max_main_diagonal_flag == 1):
        return 1
    elif(min_main_diagonal_flag == 1):
        return -1
    
    if(max_secondary_diagonal_flag == 1):
        return 1
    elif(min_secondary_diagonal_flag == 1):
        return -1
    
    if(full_flag == 1):
        return 0
    else:
        return 'not_terminal'
        
        


# state = [[1, -1, 1, -1, 1],
#          [-1, 1, -1, 1, -1],
#          [1, -1, 1, -1, 1],
#          [1, -1, 1, -1, 1],
#          [1, -1, 0, -1, 1]]

# print(utility(state=state, n=5))

        

