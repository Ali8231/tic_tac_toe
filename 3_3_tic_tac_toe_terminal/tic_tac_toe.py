import math, copy
from actions import actions
from eval import eval


def min_value(state, alpha, beta, depth_limit, current_depth):

    print(f"alpha at depth {current_depth} = ", alpha)
    print(f"beta at depth {current_depth} = ", beta, '\n')

    eval_result = eval(state, depth_limit, current_depth)
    if(eval_result != 'not_terminal'):
        return eval_result, None
    
    v = math.inf
    
    action_list = actions(state)

    for a in action_list:
        next_state = copy.deepcopy(state)

        next_state[a[0]][a[1]] = -1

        v2, a2 = max_value(next_state, alpha, beta, depth_limit, current_depth + 1)
        
        if(v2 < v):
            v, move = v2, a
            beta = min(beta, v)
        if(v <= alpha):
            print(f"***alpha cut occured in depth {current_depth}", '\n')
            return v, move
        
    return v, move



def max_value(state, alpha, beta, depth_limit, current_depth):

    print(f"alpha at depth {current_depth} = ", alpha)
    print(f"beta at depth {current_depth} = ", beta, '\n')

    eval_result = eval(state, depth_limit, current_depth)
    if(eval_result != 'not_terminal'):
        return eval_result, None
    
    v = -math.inf
    
    action_list = actions(state)
    
    for a in action_list:
        next_state = copy.deepcopy(state)

        next_state[a[0]][a[1]] = 1

        v2, a2 = min_value(next_state, alpha, beta, depth_limit, current_depth + 1)
        
        if(v2 > v):
            v, move = v2, a
            alpha = max(alpha, v)
        if(v >= beta):
            print(f"***beta cut occured in depth {current_depth}", '\n')
            return v, move
        
    return v, move

        


def alpha_beta_search(state, player, depth_limit):
    if(player == 'max'):
        value, move = max_value(state=state, alpha=-math.inf, beta=math.inf, 
                                depth_limit=depth_limit, current_depth=0)
    else:
        value, move = min_value(state=state, alpha=-math.inf, beta=math.inf, 
                                depth_limit=depth_limit, current_depth=0)

    return move



# state = [[0 for x in range(3)] for y in range((3))]
# print(alpha_beta_search(state=state, player='min', depth_limit=1))



