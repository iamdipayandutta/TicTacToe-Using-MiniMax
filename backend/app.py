from flask import Flask, request, jsonify

app = Flask(__name__)

# Initialize game state
game_state = {"board": ["" for _ in range(9)], "turn": "X", "winner": None}

def check_winner(board):
    """Check if there is a winner."""
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    for a, b, c in win_conditions:
        if board[a] and board[a] == board[b] == board[c]:
            return board[a]
    return None

@app.route("/move", methods=["POST"])
def make_move():
    global game_state
    data = request.get_json()

    # Validate request data
    if "index" not in data or not isinstance(data["index"], int):
        return jsonify({"error": "Invalid request"}), 400

    index = data["index"]

    # Validate move index
    if index < 0 or index >= 9:
        return jsonify({"error": "Index out of bounds"}), 400

    # Check if move is valid
    if game_state["winner"] or game_state["board"][index]:
        return jsonify({"error": "Invalid move"}), 400

    # Make the move
    game_state["board"][index] = game_state["turn"]
    game_state["winner"] = check_winner(game_state["board"])

    # Switch turn if no winner
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
    app.run(host="0.0.0.0", port=8080, debug=True)  # Added debug mode
