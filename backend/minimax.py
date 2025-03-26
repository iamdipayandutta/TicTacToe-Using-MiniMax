from .game_logic import check_winner, is_draw

def get_available_moves(board):
    moves = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                moves.append((i, j))
    return moves

def minimax(board, depth, is_maximizing):
    if check_winner(board) == 'X':
        return 10 - depth
    elif check_winner(board) == 'O':
        return depth - 10
    elif is_draw(board):
        return 0

    if is_maximizing:
        best_score = float('-inf')
        for i, j in get_available_moves(board):
            board[i][j] = 'X'
            score = minimax(board, depth + 1, False)
            board[i][j] = ' '
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i, j in get_available_moves(board):
            board[i][j] = 'O'
            score = minimax(board, depth + 1, True)
            board[i][j] = ' '
            best_score = min(score, best_score)
        return best_score

def get_best_move(board):
    best_score = float('-inf')
    best_move = None
    for i, j in get_available_moves(board):
        board[i][j] = 'X'
        score = minimax(board, 0, False)
        board[i][j] = ' '
        if score > best_score:
            best_score = score
            best_move = (i, j)
    return best_move
