def actions(state):
        available_actions = []

        for (i,row) in enumerate(state):
            for (j,value) in enumerate(row):
                if(value == 0):
                    available_actions.append((i, j))

        return available_actions



# state = [[0, 1, -1],
#          [-1, 0, 1],
#          [1, 1, 0]]

# print(actions(state))