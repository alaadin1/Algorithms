import math
import copy

X = "X"
O = "O"
EMPTY = None

def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

def player(board):
    """
    Returns player who has the next turn on a board.
    """
    #if the number of empty is odd, X goes
    # if the number of empty is even, O goes
    count = 0
    for rows in range(len(board)):
        for columns in range(len(board)):
            if board[rows][columns] == EMPTY:
                count = count + 1
            
    if count % 2 == 0:
        return O
    else:
        return X
    


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    #iterate through the board
    #if the space is empty, add its coordiate (i,j) to a tuple of moves
    #return the list of tuples
    legal_moves = []
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == EMPTY:
                tuple_set = (i,j)
                legal_moves.append(tuple_set)
    return (legal_moves)



def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    #determine whos turn it is
    # if it is my turn, the action I take is applied to the board. Meaning the EMPTY turns to X.
    # if it is the computers turn, turn EMPTY to O.
    players_turn = player(board)
    copy_board = copy.deepcopy(board)

    if players_turn == X:
        for i in range(len(board)):
            for j in range(len(board)):
                for moves in actions(board):
                    if action == moves:
                        x_loc = action[0]
                        y_loc = action[1]
                        copy_board[x_loc][y_loc] = X
                        break
    
    elif players_turn == O:
        for i in range(len(board)):
            for j in range(len(board)):
                for moves in actions(board):
                    if action == moves:
                        x_loc = action[0]
                        y_loc = action[1]
                        copy_board[x_loc][y_loc] = O
                        break

    return copy_board




def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # we have a winner whenever we have the a row of X or O or a column of X or O
    # Now how do we represetn that? instead of iterating through each cell, we iterate through the row
    # if the row has all X's we have a win
    # Now we iterate through the colums
    # if the columns has all X;s we have a win and we return the player

    #Winning scenerios for the X player
    #Winning rows
    for row in board:
        if row[0] == X and row[1] == X and row[2] == X:
            return X
    
    for row in board:
        if row[0] == O and row[1] == O and row[2] == O:
            return O

    #Winning coloumns
    if board[0][0] == X and board [1][0] == X and board[2][0] == X:
        return X
    elif board[0][1] == X and board[1][1] == X and board[2][1] == X:
        return X
    elif board[0][2] == X and board [1][2] == X and board [2][2] == X:
        return X
    
    #Winning diagnol
    elif board[0][0] == X and board[1][1] == X and board[2][2] == X:
        return X
    elif board[0][2] == X and board[1][1] == X and board [2][0] == X:
        return X


    #Winning scenerios for the O player
    #Winning rows
    
    
    #Winning coloumns
    elif board[0][0] == O and board [1][0] == O and board[2][0] == O:
        return O
    elif board[0][1] == O and board[1][1] == O and board[2][1] == O:
        return O
    elif board[0][2] == O and board [1][2] == O and board [2][2] == O:
        return O

    elif board[0][0] == O and board[1][1] == O and board[2][2] == O:
        return O
    elif board[0][2] == O and board[1][1] == O and board [2][0] == O:
        return O
    else:
        return None



def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    game_won = winner(board)
    count = 0

    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == EMPTY:
                count = count + 1

    if game_won == X or game_won == O or count == 0:
        return True
    else:
        return False



def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    if terminal(board) == True:
        return None

    #maxmize player
    alpha = -math.inf
    beta = math.inf
    opt_move = None
    # X is the maximizing player
    if player(board) == X:
        best_score = -math.inf

        #iterate through all the legal moves to decide which one gives us the max utlity
        for action in actions(board):
            move_utility = evaluation(result(board, action), alpha, beta)
            alpha = max(alpha, move_utility)

            if move_utility > best_score:
                best_score = move_utility
                opt_move = action

    elif player(board) == O:
        best_score = math.inf
        for action in actions(board):
            move_utility = evaluation(result(board, action), alpha, beta)
            alpha = max(alpha, move_utility)

            if move_utility < best_score:
                best_score = move_utility
                opt_move = action

    return opt_move

def evaluation(board, aplha, beta):
    if terminal(board):
        return utility(board)

    best_score = -math.inf
    alpha = -math.inf
    beta = math.inf

    if player(board) == X:
        for action in actions(board):
            best_score = max(best_score, evaluation(result(board,action), alpha, beta))
            alpha = max(alpha, best_score)
            if beta <= alpha:
                break
        return best_score

    elif player(board) == O:
        for action in actions(board):
            best_score = min(best_score, evaluation(result(board,action), alpha, beta))
            alpha = min(alpha, best_score)
            if beta >= alpha:
                break
        return best_score
    
    # # We have the AI (O) trying to minimize the score at the end
    # minEval = math.inf
    # maxEval = -(math.inf)
    # if player(board) == O:
    #     for action in actions(board):
    #         evaluation = minimax(result(board, action))
    #         minEval = min(minEval, evaluation)


    #     return minEval
    # elif player(board) == X:
    #     for action in actions(board):
    #         evaluation = minimax(result(board,action))
    #         maxEval = max(maxEval, evaluation)




# Given a state s:
    # MAX picks action a in ACTION(S) that produces highest value of Min_Value(Result(S,a))
    # MIN picks action a in ACTION(S) that produces highest value of Max_Value(Result(S,a)) 

    #function Max-Value(state):
    #   if Terminal state:
    #     return Utility(State)
    #   we want the value as high as possible
    #   v = -infinity
    #   for action in Action(state):
    #       v = MAX(v, MIN_Value(RESULT(state, action)))
    #   retunr v 


