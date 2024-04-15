
Evaluation function for n*n tic tac toe :

    eval = (number of rows, columns and diagonals for maximizer) - (number of rows, columns and diagonals for minimizer)

    Best case scenario for maximizer evaluation value is (2n + 2)
    and for minimizer it is -(2n + 2)
    As stated in eval.py return values for maximizer and minimizer are
    (2n + 3) and -(2n + 3) respectively.
    This way, evaluation values are between terminal values



How to play:

    It is the same as 3*3 one except that instead of a range of 0 to 2
    the range of values for row and column is 0 to n-1