from .game_logic import check_winner, is_draw, game_over
from .minimax import get_best_move
from .ui import print_board, get_player_move

def init_board():
    return [[' ' for _ in range(3)] for _ in range(3)]

def make_move(board, move, player):
    row, col = move
    if board[row][col] == ' ':
        board[row][col] = player
        return True
    return False

def main():
    board = init_board()
    current_player = 'X'

    while not game_over(board):
        print_board(board)
        if current_player == 'X':
            move = get_player_move()
        else:
            move = get_best_move(board)
        if make_move(board, move, current_player):
            current_player = 'O' if current_player == 'X' else 'X'

    print_board(board)
    winner = check_winner(board)
    if winner:
        print(f"Player {winner} wins!")
    else:
        print("It's a draw!")

if __name__ == "__main__":
    main()
