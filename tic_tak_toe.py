import numpy as np

def check_winner(board):

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] !=' ':
        return board[0][0]
        
    elif board[0][2]==board[1][1]== board[2][0] and board[0][2] !=' ':
        return board[0][2]
    
    
    for row in range(3):
        if board[row][0] == board[row][1]== board[row][2] and board[row][0] != ' ':
            return board[row][0]
        
    
    for col in range(3):
        if board[0][col] == board[1][col]== board[2][col] and board[0][row] !=' ':
            return board[0][col]
        
    return None

def print_board(board):
     for row in board:
         print(" | ".join(row))
        


def is_full(board):
    return all(cell != ' ' for row in board for cell in row)

def best_move(board):
    best_score = -float('inf')
    move = None

    for row in range(3):
        for col in range(3):
            if board[row][col] == ' ':
                board[row][col] ='O'
                score=min_max(board, 0, False, -float('inf'), float('inf'))
                board[row][col]=' '

                if score > best_score:
                    move=(row,col)
                    best_score=score
    
    return move
def min_max(board, depth, maximizer, alpha, beta):
    result = check_winner(board)

    if result == 'X':
        return -1
    if result == 'O':
        return 1
    if is_full(board):
        return 0
    
    if maximizer:
        best_score = -float('inf')
        for row in range(3):
            for col in range(3):
                if board[row][col] ==' ':
                    board[row][col]='O'
                    score = min_max(board,depth+1,False, alpha , beta)
                    board[row][col]=' '
                    best_score = max(score, best_score)
                    alpha= max(alpha,best_score)
                    if beta<=alpha:
                        break
        return best_score
    
    else:
        best_score = float('inf')
        for row in range(3):
            for col in range(3):
                if board[row][col]==' ':
                    board[row][col]='X'
                    score = min_max(board, depth+1, True, alpha,beta)
                    board[row][col]=' '
                    best_score = min(score,best_score)
                    best = min(beta,best_score)
                    if beta <= alpha:
                        break

        return best_score
    

def tic_tak_toe():
    board = np.array([[' ']*3 for _ in range(3)])

    while True: 
        print_board(board)

        row, col= map(int, input("Enter row and col: ").split())

        if board[row][col]!=' ':
            print("Cell occupied")
            continue

        
        board[row][col]='X'
        
        winner = check_winner(board)
        

        if winner == 'X' or winner == 'O':
            print_board(board)
            print(f"Player {winner} wins!")
            break

        if is_full(board):
            print_board(board)
            print("It's a draw!")
            break

        ai_move = best_move(board)
        if ai_move:
            board[ai_move] ='O'

        winner = check_winner(board)
        if winner == 'X' or winner == 'O':
            print_board(board)
            print(f"Player {winner} wins!")
            break

        if is_full(board):
            print_board(board)
            print("It's a draw!")
            break

tic_tak_toe()      