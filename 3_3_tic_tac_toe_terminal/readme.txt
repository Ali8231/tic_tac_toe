Evaluation function for 3*3 tic tac toe :

    value = (number of rows, columns and diagonals for maximizer) - (number of rows, columns and diagonals for minimizer)
    eval = value / 10

    Note that if state is a terminal function will return 0, 1 or -1.
    So the range of evaluation function must be between -1 and 1
    The best case scenario for maximizer is that it can place its next move in all rows, columns and diagonals.
    In this case value will be 8.
    Best case scenario for minimizer is -8.
    To normalize these values they are divided by 10 to give the range -0.8 to 0.8




How to play:

    User can play tic tac toe by running driver.py in terminal.
    Program prompts user to choose the player between computer and user.
    If user chooses computer two algorithms will play against each other.
    Otherwise user will play againgt algorithm.
    In user mode, user must enter each move in the following form : row,column
    in which row and column are integers between 0 and 2 separated by a comma

    Note that the starter player is always maximizer and opponent is minimizer wether starter is computer
    or user




