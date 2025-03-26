def print_board(board):
    print("\n")
    for i, row in enumerate(board):
        print(" " + " | ".join(row))
        if i < 2:
            print("-" * 9)
    print("\n")

def get_player_move():
    while True:
        try:
            move = input("Enter your move (row[0-2] column[0-2]): ")
            row, col = map(int, move.split())
            if 0 <= row <= 2 and 0 <= col <= 2:
                return (row, col)
            print("Move must be between 0 and 2")
        except (ValueError, IndexError):
            print("Please enter two numbers between 0 and 2, separated by space")
