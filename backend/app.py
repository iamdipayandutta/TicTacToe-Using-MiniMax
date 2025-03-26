from flask import Flask, request, jsonify
from flask_cors import CORS  

app = Flask(__name__)
CORS(app)

game_state = {"board": ["" for _ in range(9)], "turn": "X", "winner": None}

def check_winner(board):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    for a, b, c in win_conditions:
        if board[a] and board[a] == board[b] == board[c]:
            return board[a]
    return None

def minimax(board, depth, is_maximizing):
    scores = {
        "X": -1,
        "O": 1,
        "tie": 0
    }
    
    winner = check_winner(board)
    if winner:
        return scores[winner]
    
    if "" not in board:
        return scores["tie"]
        
    if is_maximizing:
        best_score = float('-inf')
        for i in range(9):
            if board[i] == "":
                board[i] = "O"
                score = minimax(board, depth + 1, False)
                board[i] = ""
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(9):
            if board[i] == "":
                board[i] = "X"
                score = minimax(board, depth + 1, True)
                board[i] = ""
                best_score = min(score, best_score)
        return best_score

def find_best_move(board):
    best_score = float('-inf')
    best_move = None
    
    for i in range(9):
        if board[i] == "":
            board[i] = "O"
            score = minimax(board, 0, False)
            board[i] = ""
            if score > best_score:
                best_score = score
                best_move = i
    
    return best_move

@app.route("/move", methods=["POST"])
def make_move():
    global game_state
    data = request.get_json()

    if "index" not in data or not isinstance(data["index"], int):
        return jsonify({"error": "Invalid request"}), 400

    index = data["index"]

    if index < 0 or index >= 9:
        return jsonify({"error": "Index out of bounds"}), 400

    if game_state["winner"] or game_state["board"][index]:
        return jsonify({"error": "Invalid move"}), 400

    game_state["board"][index] = game_state["turn"]
    game_state["winner"] = check_winner(game_state["board"])

    if game_state["winner"] is None and "" in game_state["board"]:
        game_state["turn"] = "O"
        ai_move = find_best_move(game_state["board"])
        game_state["board"][ai_move] = "O"
        game_state["winner"] = check_winner(game_state["board"])
        game_state["turn"] = "X"
    
    return jsonify(game_state)

@app.route("/reset", methods=["POST"])
def reset_game():
    global game_state
    game_state = {"board": ["" for _ in range(9)], "turn": "X", "winner": None}
    return jsonify(game_state)

@app.route("/state", methods=["GET"])
def get_state():
    return jsonify(game_state)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
