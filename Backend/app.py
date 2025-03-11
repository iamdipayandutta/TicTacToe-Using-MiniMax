from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

def minimax(board, depth, is_maximizing):
    scores = {'X': -1, 'O': 1, 'tie': 0}
    
    if check_win(board, 'X'):
        return scores['X']
    if check_win(board, 'O'):
        return scores['O']
    if is_board_full(board):
        return scores['tie']
    
    if is_maximizing:
        best_score = -float('inf')
        for i in range(9):
            if board[i] == '':
                board[i] = 'O'
                score = minimax(board, depth + 1, False)
                board[i] = ''
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(9):
            if board[i] == '':
                board[i] = 'X'
                score = minimax(board, depth + 1, True)
                board[i] = ''
                best_score = min(score, best_score)
        return best_score

def check_win(board, player):
    win_patterns = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    return any(all(board[i] == player for i in pattern) for pattern in win_patterns)

def is_board_full(board):
    return all(cell != '' for cell in board)

@app.route('/move', methods=['POST'])
def get_move():
    data = request.json
    board = data['board']
    
    best_score = -float('inf')
    best_move = -1
    
    for i in range(9):
        if board[i] == '':
            board[i] = 'O'
            score = minimax(board, 0, False)
            board[i] = ''
            if score > best_score:
                best_score = score
                best_move = i
                
    return jsonify({'move': best_move})

if __name__ == '__main__':
    app.run(debug=True)