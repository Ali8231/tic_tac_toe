import math, copy
from utility import utility
from actions import actions
from eval import eval


def min_value(state, player, alpha, beta, depth_limit, current_depth):
    eval_result = eval(state, depth_limit, current_depth)
    if(eval_result != 'not_terminal'):
        #print("reached terminal with value = ", utility_result, "\n")
        return eval_result, None
    
    v = math.inf
    
    action_list = actions(state)
    next_state = copy.deepcopy(state)
    #print("starting state befor action iteration = ", state, "\n")

    for a in action_list:
        next_state = copy.deepcopy(state)
        next_state[a[0]][a[1]] = -1
        #print("next state(minimizer) = ", next_state, "\n")

        v2, a2 = max_value(next_state, player, alpha, beta, depth_limit, current_depth + 1)
        
        if(v2 < v):
            v, move = v2, a
            #print("move = ", move)
            beta = min(beta, v)
        if(v <= alpha):
            return v, move
        
    #print("move = ", move)
    return v, move



def max_value(state, player, alpha, beta, depth_limit, current_depth):
    eval_result = eval(state, depth_limit, current_depth)
    if(eval_result != 'not_terminal'):
        #print("reached terminal with value = ", utility_result, "\n")
        return eval_result, None
    
    v = -math.inf
    
    action_list = actions(state)
    next_state = copy.deepcopy(state)
    #print("starting state befor action iteration = ", state, "\n")

    for a in action_list:
        next_state = copy.deepcopy(state)
        #print("state = ", state, "\n")

        next_state[a[0]][a[1]] = 1
        #print("next state(maximizer) = ", next_state, "\n")

        v2, a2 = min_value(next_state, player, alpha, beta, depth_limit, current_depth + 1)
        
        if(v2 > v):
            v, move = v2, a
            #print("move = ", move)
            alpha = max(alpha, v)
        if(v >= beta):
            return v, move
        
    #print("move = ", move)
    return v, move

        


def alpha_beta_search(state, player, depth_limit):
    if(player == 'max'):
        #print("started as max")
        value, move = max_value(state, player, -math.inf, math.inf, depth_limit, 0)
    else:
        #print("started as min")
        value, move = min_value(state, player, -math.inf, math.inf, depth_limit, 0)

    return move



# state = [[0 for x in range(3)] for y in range((3))]
# print(alpha_beta_search(state=state, player='max', depth_limit=math.inf))



