from flask import Flask, request, jsonify

app = Flask(__name__)

game_state = {"board": ["" for _ in range(9)], "turn": "X", "winner": None}

def check_winner(board):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    for condition in win_conditions:
        a, b, c = condition
        if board[a] and board[a] == board[b] == board[c]:
            return board[a]
    return None

@app.route("/move", methods=["POST"])
def make_move():
    global game_state
    data = request.get_json()
    index = data.get("index")
    
    if game_state["winner"] or game_state["board"][index]:
        return jsonify({"error": "Invalid move"}), 400
    
    game_state["board"][index] = game_state["turn"]
    game_state["winner"] = check_winner(game_state["board"])
    
    if game_state["winner"] is None:
        game_state["turn"] = "O" if game_state["turn"] == "X" else "X"
    
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
    app.run(host="0.0.0.0", port=8080)