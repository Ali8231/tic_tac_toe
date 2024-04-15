import math, copy, time
from utility import utility
from actions import actions
from eval import eval


def min_value(state, n, alpha, beta, depth_limit, current_depth):
    eval_result = eval(state, n, depth_limit, current_depth)
    if(eval_result != 'not_terminal'):
        return eval_result, None
    
    v = math.inf
    
    action_list = actions(state)

    for a in action_list:
        next_state = copy.deepcopy(state)

        next_state[a[0]][a[1]] = -1

        v2, a2 = max_value(next_state, n, alpha, beta, depth_limit, current_depth + 1)
        
        if(v2 < v):
            v, move = v2, a
            beta = min(beta, v)
        if(v <= alpha):
            return v, move
        
    return v, move



def max_value(state, n, alpha, beta, depth_limit, current_depth):
    eval_result = eval(state, n, depth_limit, current_depth)
    if(eval_result != 'not_terminal'):
        return eval_result, None
    
    v = -math.inf
    
    action_list = actions(state)

    for a in action_list:
        next_state = copy.deepcopy(state)

        next_state[a[0]][a[1]] = 1

        v2, a2 = min_value(next_state, n, alpha, beta, depth_limit, current_depth + 1)
        
        if(v2 > v):
            v, move = v2, a
            alpha = max(alpha, v)
        if(v >= beta):
            return v, move
        
    return v, move

        


def alpha_beta_search(state, n, player, depth_limit):
    if(player == 'max'):
        value, move = max_value(state, n, -math.inf, math.inf, depth_limit, 0)
    else:
        value, move = min_value(state, n, -math.inf, math.inf, depth_limit, 0)

    return move








def min_value_minimax(state, n, depth_limit, current_depth):
    eval_result = eval(state, n, depth_limit, current_depth)
    if(eval_result != 'not_terminal'):
        return eval_result, None
    
    v, move = math.inf, math.inf
    
    action_list = actions(state)

    for a in action_list:
        next_state = copy.deepcopy(state)

        next_state[a[0]][a[1]] = -1

        v2, a2 = max_value_minimax(next_state, n, depth_limit, current_depth + 1)
        
        if(v2 < v):
            v, move = v2, a
        
    return v, move



def max_value_minimax(state, n, depth_limit, current_depth):
    eval_result = eval(state, n, depth_limit, current_depth)
    if(eval_result != 'not_terminal'):
        return eval_result, None
    
    v, move = -math.inf, -math.inf
    
    action_list = actions(state)

    for a in action_list:
        next_state = copy.deepcopy(state)

        next_state[a[0]][a[1]] = 1

        v2, a2 = min_value_minimax(next_state, n, depth_limit, current_depth + 1)
        
        if(v2 > v):
            v, move = v2, a
        
    return v, move



def minimax_search(state, n, player, depth_limit):
    if(player == 'max'):
        value, move = max_value_minimax(state, n, depth_limit, 0)
    else:
        value, move = min_value_minimax(state, n, depth_limit, 0)

    return move







start_time = time.time()
state = [[0 for x in range(4)] for y in range((4))]
print('\n', "move =", alpha_beta_search(state=state, n=4, player='max', depth_limit=4))
end_time = time.time()
alpha_beta_elapsed_time = end_time - start_time
print("alpha_beta algorithm elapsed time = ", alpha_beta_elapsed_time)


start_time = time.time()
state = [[0 for x in range(4)] for y in range((4))]
print('\n', "move =", minimax_search(state=state, n=4, player='max', depth_limit=4))
end_time = time.time()
minimax_elapsed_time = end_time - start_time
print("minimax algorithm elapsed time = ", minimax_elapsed_time)

print("\nalpha beta / minimax elapsed time = ", alpha_beta_elapsed_time/minimax_elapsed_time)




