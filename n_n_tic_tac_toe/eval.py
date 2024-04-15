
# eval function acts similar to utility for
# a terminal condition except that insted of 
# 1 it returns (2n + 3) for maximizer, instead
# of -1 it returns -(2n + 3) for minimizer and
# 0 if board is full. If it is not a terminal 
# condition and current depth is greater than
# depth limit function returns an evaluation 
# value. this evaluation is explained in readme
# file. otherwise it will return not_terminal
# this function has all the terminal flags in 
# utility function. Furthermore it includes flags
# for incrementing evaluation values

def eval(state, n, depth_limit, current_depth):
    
    full_flag = 1

    max_main_diagonal_flag = 1
    min_main_diagonal_flag = 1

    max_secondary_diagonal_flag = 1
    min_secondary_diagonal_flag = 1

    max_eval_value = 0
    min_eval_value = 0

    max_eval_main_diagonal_flag = 1
    min_eval_main_diagonal_flag = 1

    max_eval_secondary_diagonal_flag = 1
    min_eval_secondary_diagonal_flag = 1

    for row in range(n):
        max_row_flag = 1
        min_row_flag = 1

        max_col_flag = 1
        min_col_flag = 1

        max_eval_row_flag = 1
        min_eval_row_flag = 1

        max_eval_col_flag = 1
        min_eval_col_flag = 1

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


            if(state[row][col] == -1):
                max_eval_row_flag = 0
            if(state[row][col] == 1):
                min_eval_row_flag = 0

            if(state[col][row] == -1):
                max_eval_col_flag = 0
            if(state[col][row] == 1):
                min_eval_col_flag = 0

            if((row == col) and (state[row][col] == -1)):
                max_eval_main_diagonal_flag = 0
            if((row == col) and (state[row][col] == 1)):
                min_eval_main_diagonal_flag = 0

            if((row + col == n-1) and (state[row][col] == -1)):
                max_eval_secondary_diagonal_flag = 0
            if((row + col == n-1) and (state[row][col] == 1)):
                min_eval_secondary_diagonal_flag = 0


        if(max_row_flag == 1):
            return ((2 * n) + 3)
        elif(min_row_flag == 1):
            return -((2 * n) + 3)
        
        if(max_col_flag == 1):
            return ((2 * n) + 3)
        elif(min_col_flag == 1):
            return -((2 * n) + 3)
        

        if(max_eval_row_flag == 1):
            max_eval_value += 1
        if(min_eval_row_flag == 1):
            min_eval_value += 1

        if(max_eval_col_flag == 1):
            max_eval_value += 1
        if(min_eval_col_flag == 1):
            min_eval_value += 1

        
    if(max_main_diagonal_flag == 1):
        return ((2 * n) + 3)
    elif(min_main_diagonal_flag == 1):
        return -((2 * n) + 3)
    
    if(max_secondary_diagonal_flag == 1):
        return ((2 * n) + 3)
    elif(min_secondary_diagonal_flag == 1):
        return -((2 * n) + 3)
    
    if(full_flag == 1):
        return 0
    

    if(max_eval_main_diagonal_flag == 1):
        max_eval_value += 1
    if(min_eval_main_diagonal_flag == 1):
        min_eval_value += 1

    if(max_eval_secondary_diagonal_flag == 1):
        max_eval_value += 1
    if(min_eval_secondary_diagonal_flag == 1):
        min_eval_value += 1
    


    if(current_depth > depth_limit):

        sum = max_eval_value - min_eval_value

        return sum
    
    return 'not_terminal'




# state = [[1, -1, -1, -1, 1],
#          [1, -1, -1, 1, 1],
#          [1, 1, 1, 1, 1],
#          [1, 1, -1, 1, 1],
#          [-1, 1, 1, 1, 1]]


# print(eval(state = state, n=5, depth_limit = 10, current_depth = 8))
